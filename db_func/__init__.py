from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) 

# Reason for using packages - for example, you don't need to run this app.push() func in every function called. 
app.app_context().push()

# Also, without packages, you will have to import app and db to every function called. 