from authors_app import db

class User(db.Model):
    __table__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    first_name= db.Column(db.String(50), nullable=False)
    last_name= db.Column(db.String(100), nullable=False)
    email= db.Column(db.string(100), nullable= False, unique=True)
    contact= db.Column(db.Integer(50), nullable= False, unique=True)
    user_type= db.Column(db.string(100), nullable=False)
    image= db.Column(db.String(255), nullable=false)
    