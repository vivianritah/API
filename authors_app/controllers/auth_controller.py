from flask import Blueprint, request, jsonify, session
from authors_app.models.user import User
from authors_app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@auth.route('/register', methods=['POST'])
def register():
    try:
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        email = request.json.get('email') 
        contact = request.json.get('contact')
        password = request.json.get('password')
        image = request.json.get('image')
        user_type = request.json.get('user_type')
        biography = request.json.get('biography')  # Retrieve biography from request data

        if not first_name:
            return jsonify({"error": "Your first name is required"})
        if not last_name:
            return jsonify({"error": "Your last name is required"})
        if not email:
            return jsonify({"error": "Your email is required"})
        if not contact:
            return jsonify({"error": "Your contact is required"})
        if len(password) < 8:
            return jsonify({"error": "Your password should have at least 8 characters"})
        if user_type == 'author' and not biography:
            return jsonify({"error": "Your biography is required"})
        if not user_type:
            return jsonify({"error": "Your user_type is required"})

        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'})
        if User.query.filter_by(contact=contact).first():
            return jsonify({'error': 'Contact already exists'})

        new_user = User(
            last_name=last_name,
            first_name=first_name,
            email=email,
            password=password,  
            contact=contact,
            image=image,
            user_type=user_type,
            biography=biography  # Pass biography to User constructor
        )

        db.session.add(new_user)
        db.session.commit()

        username = f"{new_user.first_name} {new_user.last_name}"

        return jsonify({
            'message': f'{username} has been successfully created as an {new_user.user_type}',
            'user': {
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email,
                'contact': new_user.contact,
                'password': new_user.password,
                'biography':new_user.biography,
                'type': new_user.user_type,
                'created_at': new_user.created_at
            }
        })



    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)})


@auth.route('/user/<int:user_id>', methods=["GET"])
    # getting a specfic user
def get_user(user_id):
        try:
            # Query the user from the database by user ID
            # trying to get a pecific user by passing in their user_id
            user = User.query.get(user_id)

            # Check if the user exists
            if user:
                # Serialize the user data
                serialized_user = {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'image': user.image,
                    'biography': user.biography,
                    'user_type': user.user_type,
                    'contact': user.contact,
                    'password':user.password
                }
                # Return the serialized user data
                return jsonify({'user': serialized_user}), 200
            else:
                return jsonify({'error': 'User not found'}), 404

        except Exception as e:
            return jsonify({'error': str(e)}), 50


# Getting all users
@auth.route('/users', methods=["GET"])
def get_all_users():
    try:
        # Query all users from the database
        users = User.query.all()

        # Serialize users data im other words convert data into a format suitable for storage
        serialized_users = []
        for user in users:
            serialized_user = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'image': user.image,
                'biography': user.biography,
                'user_type': user.user_type,
                'contact': user.contact,
                'password':user.password
            }
            serialized_users.append(serialized_user)

        # Return the serialized users data
        return jsonify({'users': serialized_users}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Deleting the user
@auth.route('/delete/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit() #pushes to the database

        return jsonify({'message': 'User deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@auth.route("/<int:id>") 
@jwt_required()
def get_book(id):
    try:
        current_user = get_jwt_identity()  # Get current user using get_jwt_identity
        book = User.query.filter_by(user_id=current_user, id=id).first()

        if not book:
            return jsonify({'error': 'Item not found'}), 404
        
        # Return book details
        return jsonify({
            'first_name': current_user.first_name,
                'last_name': current_user.last_name,
                'email': current_user.email,
                'contact': current_user.contact,
                ' user_type': current_user.user_type,
                'biography': current_user.biography,
                'image':current_user.image,
                'password':current_user.password,
                'created_at': current_user.created_at,
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500    






