from authors_app import db


class company(db.model):
 __table__="company"
id =db.Column(db.Integer,primay_key=True)
name=db.Column(db.String(50),nallable=False,unique=True)
description=db.Column(db.String(100),nallable=False)
user_id =db.Column(db.Integer,db.foreign_key("user_id"))