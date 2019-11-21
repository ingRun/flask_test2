from flask import Flask
import os

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from app import models, urls


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(id=user_id)



