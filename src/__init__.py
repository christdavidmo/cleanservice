from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_mail import Mail

import os
from config import Config  
from  .extensions import db , migrate ,mail


# Initialisation de l'objet db (SQLAlchemy) et migrate (Flask-Migrate)
# db = SQLAlchemy()
# migrate = Migrate()
# mail = Mail()

def create_app(config_class=Config):


    # Initialisation de l'application Flaskclear
    app = Flask(__name__)

    # Chargement des configurations depuis Config
    app.config.from_object(config_class)

    # Initialisation de la base de données et de Flask-Migrate
    db.init_app(app)
    migrate.init_app(app, db)



    # Création des tables dans la base de données
    # with app.app_context():
    #     print("Modèles enregistrés avant création :", db.Model.metadata.tables.keys())
    #     db.create_all()
    #     print("Tables créées avec succès !")
    
    
    
    
    # Configuration de l'upload des images
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')  
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)  # Crée le dossier s'il n'existe pas
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Enregistrement des routes (ou blueprints)
    from .routes import bp  # Assure-toi que ce fichier `routes.py` existe et contient les bonnes routes
    app.register_blueprint(bp)

    return app
