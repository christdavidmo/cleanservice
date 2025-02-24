from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def creat_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .models import User,Address

    from . import routes
    app.register_blueprint(routes.bp)

    return app
