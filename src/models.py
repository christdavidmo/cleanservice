# from flask_sqlalchemy import SQLAlchemy
from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

# Initialisation de la base de données
# db = SQLAlchemy()



# ======= =======================
# connexion de l'utilisateur  ? 
# ======= =======================
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(225), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"User(id={self.id}, login={self.login})"

# ======= =======================
# connexion de l'utilisateur  ? 
# ======= =======================




class Information(db.Model):
    __tablename__ = 'informations'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    # about_us = db.Column(db.Text, nullable=True)

    # Relation avec les numéros de téléphone
    telephones = db.relationship('Telephone', backref='business', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"InformationBusiness(id={self.id}, email={self.email}, about_us={self.about_us})"

#===================
# barre du bas 
#===================

class Ouverture(db.Model):
    __tablename__ = 'ouvertures'
    id = db.Column(db.Integer, primary_key=True)
    jour = db.Column(db.String(50), nullable=False)  # Retirer unique=True pour permettre plusieurs horaires par jour
    heure_ouverture = db.Column(db.String(50), nullable=False)
    heure_fermeture = db.Column(db.String(50), nullable=False)

#===================================
# barre du bas 
#===================================


#====== Télephone
class Telephone(db.Model):
    __tablename__ = 'telephones'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(15), unique=True, nullable=True)
    business_id = db.Column(db.Integer, db.ForeignKey('informations.id'), nullable=False)

    def __repr__(self):
        return f"Telephone(id={self.id}, number={self.number}, business_id={self.business_id})"
#====== Télephone


#======  lien reseaux instagram facebook whatsapp
class Reseau(db.Model):
    __tablename__ = 'reseaux'
    id = db.Column(db.Integer, primary_key=True)
    lien = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Reseau(lien={self.lien})"
#======  lien reseaux instagram facebook whatsapp


#===================================
# barre du bas 
#===================================



# ======= ===========
# tous les services ? 
# ======= ===========
class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    nameService = db.Column(db.String(100), nullable=False)
    priceService = db.Column(db.Float)
    imageservice = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"Service(id={self.id}, nameService={self.nameService}, priceService={self.priceService}, imageservice={self.imageservice})"
# ======= ===========
# tous les services ? 
# ======= ===========



# ======= =========
# pourquoi nous ? 
# ======= =========
class WhyUs(db.Model):
    __tablename__ = 'why_us'
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.Text, nullable=False)  # Chaque raison est un texte modifiable
# ======= =========
# pourquoi nous ? 
# ======= =========


# ===============
# MESSAGE
# ===============

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)  # Messages laissés par les clients

# ===============
# MESSAGE
# ===============




# =========== ===============
# texte dans la page ABOUT US
# =========== ===============
class AboutUsContent(db.Model):
    __tablename__ = 'about_us_content'
    id = db.Column(db.Integer, primary_key=True)
    paragraph = db.Column(db.Text, nullable=False)  # Chaque paragraphe de la page "À propos de nous"

    def __repr__(self):
        return f"AboutUsContent(id={self.id}, paragraph={self.paragraph})"
# =========== ===============
# texte dans la page ABOUT US
# =========== ===============



# =========== ===============
# texte dans la page SERVICE
# =========== ===============
class ServiceContent(db.Model):
    __tablename__ = 'service_content'
    id = db.Column(db.Integer, primary_key=True)
    paragraph = db.Column(db.Text, nullable=False)  # Chaque paragraphe de la page "Services"
# =========== ===============
# texte dans la page SERVICE
# =========== ===============



# =========== =============== ===================
# GESTION DES QUESTIONS ET REPONSE DE LA PAGE FAQ
# =========== =============== ===================
class FAQQuestion(db.Model):
    __tablename__ = 'faq_questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    frequency = db.Column(db.Integer, default=0)  # Fréquence des questions posées
    # Relation avec les réponses
    answers = db.relationship('FAQAnswer', backref='question', lazy=True)

class FAQAnswer(db.Model):
    __tablename__ = 'faq_answers'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('faq_questions.id'), nullable=False)
    answer = db.Column(db.Text, nullable=False)

# =========== =============== ===================
# GESTION DES QUESTIONS ET REPONSE DE LA PAGE FAQ
# =========== =============== ===================