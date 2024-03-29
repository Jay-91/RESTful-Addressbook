from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow

import os

# Init app
app = Flask(__name__)
api = Api(app)

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)






