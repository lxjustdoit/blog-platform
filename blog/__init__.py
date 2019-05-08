from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f6a866614b91458e13dcabb88a8bfd15'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) 
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@app.before_first_request
def create_tables():
    from blog.models import ContactModel
    db.create_all()

from blog import routes,models