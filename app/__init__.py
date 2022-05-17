from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# p = os.environ.get('SECRET_KEY')
app = Flask(__name__, template_folder='./templates')

# app.secret_key = '\xea\x1a\xb2\x8a\xefk\xd6V%\xf7\xb4\xe5\xa9\r=&'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:linux123@localhost/radio'  ## postgres ://nazwa uzytkownima : haslo @ localhost/nazwa bazy danych
app.config['SECRET_KEY'] = 'f027a3f2e1b601db1ae08006930c074f'
db = SQLAlchemy(app)

from app import routes
