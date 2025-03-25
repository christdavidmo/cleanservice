from .models import *
import os
from flask import current_app
from werkzeug.utils import secure_filename


# ==== ajout d'informations ====
def add_information_business (Email , About_us) :
    business = Information(email = Email , about_us = About_us)
    db.session.add(business)
    db.session.commit()
    return business

# ==== Afficher informations ====
def getInformation():
    return Information.query.first()

# ==== Mofifier informations ====
def Update_Information(New_Email  = None, New_About = None):

    infos = Information.query.first()

    if infos :
        if New_Email :
            infos.email = New_Email
        if  New_About :
            infos.about_us = New_About
        db.session.commit()
        return infos
    return None






# ==== ajout numero ====
def add_numero( Number , Business_id):
    telephone = Telephone( number = Number , business_id = Business_id )
    db.session.add(telephone)
    db.session.commit()
    return telephone

# ==== Afficher numero ===
def get_Numero():
    return Telephone.query.first()

# ==== Modifier numero ===


# ==== Delete numero ===
def Delete_Numero( Numero_Id):
    tel = Telephone.query.get(Numero_Id)

    if tel :
        db.session.delete(tel)
        db.session.commit()
        return True 
    return False









# ==== ajout user ====
def add_user(Login , Password):
    user = User( login = Login , password = Password)
    db.session.add(user)
    db.session.commit()
    return user

# ==== Modifier user ====
def Update_User(login, NEW_LOGIN = None ,NEW_PASSWORD = None):
    user = User.query.filter_by(login = login).first()

    if user :
        if NEW_LOGIN :
            user.login = NEW_LOGIN
        if NEW_PASSWORD :
            user.passwored = NEW_PASSWORD
        db.session.commit()
        return user
    return None


# trouver user via id 
def findUserByLogin(login):
    return  User.query.filter_by(login = login).first()

# ==== Supprimer user ====   
def Delete_User(login):
    user = findUserByLogin(login)

    if user :
        db.session.delete(user)
        db.session.commit()
        return True
    return " l'utilisateur que vous cherchez à supprimer n'existe pas ou plus dans la BD"




# ==== Lister service ====
def getservice():
    return Service.query.all()

# ==== ajout service ====
import os
def add_Service(Name_service, Prix_Service, Image_file):
    try:
        #Vérifier si une image a été fournie
        if Image_file:
            
            #Définir le dossier de destination
            upload_folder = "/uploads"
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)  # Crée le dossier si nécessaire

            #Définir le chemin complet où l'image sera stockée
            image_filename = os.path.join(upload_folder, Image_file.filename)

            #Sauvegarder l'image
            Image_file.save(image_filename)
        else:
            image_filename = None  # Aucune image fournie

        #Créer et enregistrer le service dans la base de données
        service = Service(
            nameService=Name_service,
            priceService=Prix_Service,
            imageservice=image_filename  # Enregistre le chemin de l'image
            
        )

        db.session.add(service)
        db.session.commit()

        return service

    except Exception as e:
        print(f"Erreur lors de l'ajout du service : {e}")
        return None
    



# === ajouter texte pourquoi nous ? ===
def add_WhyUs(nouvelleRaison):
    raison = WhyUs( reason = nouvelleRaison)
    db.session.add(raison)
    db.session.commit()
    return raison

# === trouver texte pourquoi nous ? ===
def find_Why_Us(ID):
   return WhyUs.query.filter_by(id = ID).first()


# === supprimer texte pourquoi nous ? ===
def delete_Why_Us(ID):
    raison  = find_Why_Us(ID)
    if raison :
        db.session.delete(raison)
        db.session.commit()
        return True
    return "Cette raison a bien été supprimée"

# == mettre à jour ===
def update_WhyUs(ID, nouvelleRaison):
    raison = find_Why_Us(ID)
    if raison:
        raison.reason = nouvelleRaison
        db.session.commit()
        return raison
    return "Raison introuvable."

# ===  afficher toutes les raisons
def get_all_WhyUs():
    return WhyUs.query.all()






# ===  ajouter message ====
def addMessage( nouveauMessage):
    message = Message( content = nouveauMessage)
    db.session.add(message)
    db.session.commit()
    return message


# ==== trouver message ===
def find_message(ID):
    return Message.query.filter_by(id = ID).first()

# ===  supprimer message ====
def delete_message(ID):
    message = find_message(ID)

    if message :
        db.session.delete(message)
        db.session.commit()
        return True
    return "Message supprimé"
# == mettre à jour un message == 
def update_message(ID, nouveauMessage):
    message = find_message(ID)
    if message:
        message.content = nouveauMessage
        db.session.commit()
        return message
    return "Message introuvable."

# == afficher tous les messages ==
def get_all_messages():
    return Message.query.all()






# == ajouter un texte à propos de nous 
def add_about_us(paragraph):
    content = AboutUsContent(paragraph=paragraph)
    db.session.add(content)
    db.session.commit()
    return content

# == afficher tous les textes
def get_about_us_content():
    return AboutUsContent.query.all()

# == trouver 
def find_about_us(ID):
    return AboutUsContent.query.filter_by(id=ID).first()

# == mettre à jour 
def update_about_us(ID, nouveau_paragraph):
    paragraph = find_about_us(ID)
    if paragraph:
        paragraph.paragraph = nouveau_paragraph
        db.session.commit()
        return paragraph
    return "Paragraphe introuvable."

# === supprimer 
def delete_about_us(ID):
    paragraph = find_about_us(ID)
    if paragraph:
        db.session.delete(paragraph)
        db.session.commit()
        return True
    return "Paragraphe introuvable."







def add_service_content(paragraph):
    content = ServiceContent(paragraph=paragraph)
    db.session.add(content)
    db.session.commit()
    return content


def get_service_content():
    return ServiceContent.query.all()

def find_service_content(ID):
    return ServiceContent.query.filter_by(id=ID).first()

def update_service_content(ID, nouveau_paragraph):
    paragraph = find_service_content(ID)
    if paragraph:
        paragraph.paragraph = nouveau_paragraph
        db.session.commit()
        return paragraph
    return "Paragraphe introuvable."

def delete_service_content(ID):
    paragraph = find_service_content(ID)
    if paragraph:
        db.session.delete(paragraph)
        db.session.commit()
        return True
    return "Paragraphe introuvable."

