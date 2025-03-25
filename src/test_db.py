import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models import * 
from src.dboperations import *
from io import BytesIO
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/cleanservicedb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def run_test():
    with app.app_context():  # Assure que le contexte Flask est actif
    #     print("Ajout des informations de l'entreprise \n ")
    #     inform = add_information_business(
    #         Email="testmail@gmail.com",
    #         About_us="À propos \n Nous ne partons que \n lorsque ça brille"
    #     )

    #     print(f"Informations ajoutées : {inform}")

    #     print("Ajout de numéro \n ")
    #     phone1 = add_numero(Number="+22112345678", Business_id=inform.id)
    #     phone2 = add_numero(Number="+22198765432", Business_id=inform.id)

    #     print(f'Numéro 1 : {phone1} , Numéro 2 : {phone2} \n')

    #     print("Ajout des services avec images : \n")
        


        
    #    # Liste des services et images associées
    #     services_data = [
    #         ("Société de nettoyagee", 80000.0, "image27.png"),
    #         ("Société de nettoyage", 80000.0, "image22.png"),
    #         ("Nettoyage de fenêtre", 80000.0, "homme-nettoyage.png"),
    #         ("Nettoyage en entreprise", 80000.0, "image24.png"),
    #         ("Nettoyage avant/après déménagement", 80000.0, "image23.png"),
    #         ("Nettoyage moquette", 80000.0, "image25.png"),
    #     ]

    #     # Vérifier si le dossier images existe
    #     images_path = "src/static/images"
    #     if not os.path.exists(images_path):
    #         print(f"❌ Le dossier {images_path} n'existe pas ! Vérifie ton projet.")
    #         return

    #     # Ajouter les services avec images
    #     for name, price, img_file in services_data:
    #         img_path = os.path.join(images_path, img_file)

    #         if not os.path.exists(img_path):
    #             print(f"❌ Image non trouvée : {img_file} (vérifie dans {images_path})")
    #             continue  # Passer au suivant si l'image est manquante

    #         with open(img_path, "rb") as img:
    #             file_storage = FileStorage(
    #                 stream=BytesIO(img.read()),  
    #                 filename=img_file,
    #                 content_type="image/png"
    #             )
    #             service = add_Service(Name_service=name, Prix_Service=price, Image_file=file_storage)
    #             print(f"✅ Service ajouté : {service}")



        wu =  add_WhyUs("Nettoyage professionnel et certifié")
        wu =  add_WhyUs("Nettoyage soucieux de l'environnement")
        wu =  add_WhyUs("100 de satisfaction garantie")
        wu =  add_WhyUs("Disponibilité le soir et le week-end")
        

        message = addMessage("j'ai bien aimé le service.Je reconseil vivement le service de nettoyage")
        message2 = addMessage("les services sont impeccables j'ai adorés")
        message3 = addMessage("merci pour votre travail et votre dévouement ")
        message4 = addMessage("éfficacité ,  rapidité , GOOD JOB!!! ")

        AboutUs1 = add_about_us("À propos \n Nous ne partons que \n lorsque ça brille")
        AboutUs2 = add_about_us("Nous croyons que la propreté va au-delà de l’apparence. Elle reflète un engagement envers le bien-être et le respect de notre environnement.")


        service1 = add_service_content("Services \n Pour nous, \n la propreté \n doit être immaculée")
        service2 = add_service_content("Nos services sont pensés pour répondre à vos besoins spécifiques avec une précision et une attention incomparables.")




# Exécuter les tests
if __name__ == "__main__":
    run_test()
