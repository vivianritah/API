from flask import Flask
from flask_sqlalchemy import SQLAlchemy




def create_app():
    app=Flask(__name__)


    @app.route('/')
    def home():
        return "Hello world"

        
    return app


