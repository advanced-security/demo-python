import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
TEMPLATES = os.path.join(ROOT, 'templates')

flaskapp = Flask("BookStore", template_folder=TEMPLATES)
flaskapp.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLITE_URI', 'sqlite:////tmp/test.db')
flaskapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flaskapp)
