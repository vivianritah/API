from authors_app import db


class books(db.model):
 __table__="books"
id =db.Column(db.Integer,primay_key=True)
title=db.Column(db.String(50),nallable=False)
description=db.Column(db.String(100),nallable=False)
image=db.Column(db.String(255),nallable=False)
price=db.column(db.Integer,nallable=False)
number_of_pages=db.Column(db.Integer,nallable=False) 