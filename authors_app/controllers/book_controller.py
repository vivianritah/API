from flask import Blueprint, Request, jsonify
from authors_app.models.books import Books

books = Blueprint('book', __name__, url_prefix='api/v1/books')  

@books.route('/register', methods=['POST'])

def register():
    title = request.json['title']
    description = request.json['description']
    publication_date= request.json['publication_date']
    image = request.json['image']
    pages = request.json['pages']
    price= request.json['price']
    company_id= request.json['company_id']
    user_id= request.json['user_id']


    if not title:
        return jsonify({'error': "Title is required"})
    if not description:
        return jsonify({'error': 'Description is required'})
    if not publication_date:
        return jsonify({'error': 'Publication date is required'})
    if not image:
        return jsonify({'error': 'Your image is required'})


# creating a new book
    new_book = Book(title=title, description=description, publication_date=publication_date,
                    image=image, pages=pages, price=price, company_id=company_id, user_id=user_id)

 

