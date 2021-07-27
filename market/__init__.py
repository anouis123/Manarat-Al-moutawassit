from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Stourism.db'
app.config['SECRET_KEY'] = '35ec4695e695d5c8c77e7c22'
db = SQLAlchemy(app)

from market import routes

