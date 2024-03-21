from authors_app.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__="users"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    contact = db.Column(db.Integer, unique=True)
    user_type = db.Column(db.String(100), nullable=False, unique=True)
    image = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False,unique=True)
    biography= db.Column(db.Text(), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    #books = db.relationship('Book', backref='user')

    def __init__(self, first_name, last_name, email, contact, user_type, password, biography, image=None):
        super(User, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.password = password
        self.user_type = user_type
        self.image = image
        self.biography=biography

 

    