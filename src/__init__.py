from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import os



db = SQLAlchemy()
mail = Mail()

def creat_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    # from .models import User,Address

    from . import routes
    app.register_blueprint(routes.bp)

    return app
