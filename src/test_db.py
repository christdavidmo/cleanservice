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
    #     inform = add_information_business(Email="testmail@gmail.com")

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



    #     wu =  add_WhyUs("Nettoyage professionnel et certifié")
    #     wu =  add_WhyUs("Nettoyage soucieux de l'environnement")
    #     wu =  add_WhyUs("100 de satisfaction garantie")
    #     wu =  add_WhyUs("Disponibilité le soir et le week-end")
    #     print(f"✅ raison ajouté : {wu }")
        

    #     message = addMessage("j'ai bien aimé le service.Je reconseil vivement le service de nettoyage")
    #     message2 = addMessage("les services sont impeccables j'ai adorés")
    #     message3 = addMessage("merci pour votre travail et votre dévouement ")
    #     message4 = addMessage("éfficacité ,  rapidité , GOOD JOB!!! ")
    #     print(f"✅ message ajouté : { message4  }")

    #     AboutUs1 = add_about_us("À propos \n Nous ne partons que \n lorsque ça brille")
    #     AboutUs2 = add_about_us("Nous croyons que la propreté va au-delà de l’apparence. Elle reflète un engagement envers le bien-être et le respect de notre environnement.")
    #     print(f"✅ a propos de nous  ajouté : { AboutUs2  }")

    #     service1 = add_service_content("Services \n Pour nous, \n la propreté \n doit être immaculée")
    #     service2 = add_service_content("Nos services sont pensés pour répondre à vos besoins spécifiques avec une précision et une attention incomparables.")
    #     print(f"✅ service ajouté : {  service2 }")


        # Ajouter les questions à la table FAQQuestion
        questions = [
            "Quels types de services de nettoyage proposez-vous ?",
            "Quels sont vos tarifs pour le nettoyage de maison ?",
            "Quels produits utilisez-vous pour le nettoyage ?",
            "Est-ce que vous nettoyez les tapis et moquettes ?",
            "Est-ce que vos services sont disponibles le week-end ?",
            "Proposez-vous un nettoyage après travaux ?",
            "Faites-vous le ménage de printemps ?",
            "Est-ce que vous proposez un nettoyage pour les appartements ?",
            "Combien de temps prend un nettoyage complet ?",
            "Est-ce que vous nettoyez les vitres ?",
            "Est-ce que vous utilisez des produits écologiques ?",
            "Est-ce que je dois être présent lors du nettoyage ?",
            "Faites-vous des réductions pour les services réguliers ?",
            "Comment réserver un service de nettoyage ?",
            "Quelles zones géographiques couvrez-vous ?",
            "Quel type de nettoyage faites-vous pour les cuisines ?",
            "Offrez-vous des services de nettoyage pour les bureaux ?",
            "Comment puis-je payer pour le service de nettoyage ?",
            "Est-ce que vous offrez un service de nettoyage d'urgence ?",
            "Que faire si je ne suis pas satisfait du nettoyage effectué ?"
        ]

        # Insérer ces questions dans la table FAQQuestion
        for question_text in questions:
            new_question = FAQQuestion(question=question_text, frequency=0)  # Ajouter avec une fréquence initiale de 0
            db.session.add(new_question)

        # Sauvegarder les questions dans la base de données
        db.session.commit()

        # Ajouter les réponses correspondantes dans la table FAQAnswer
        answers = [
            "Nous proposons du nettoyage résidentiel, commercial, après chantier, nettoyage de vitres, et bien plus encore.",
            "Nos tarifs varient selon la surface et le type de service. Veuillez nous contacter pour un devis personnalisé.",
            "Nous utilisons des produits professionnels de nettoyage, certains écologiques et d'autres spécifiques pour des surfaces particulières.",
            "Oui, nous nettoyons les tapis et les moquettes en profondeur, avec des produits adaptés.",
            "Oui, nous proposons des services de nettoyage le week-end sur demande.",
            "Oui, nous proposons un nettoyage complet après travaux, y compris l'élimination des poussières et débris.",
            "Oui, nous proposons un nettoyage de printemps, incluant une désinfection approfondie et un nettoyage général.",
            "Oui, nous offrons des services de nettoyage pour les appartements, en tenant compte des besoins spécifiques de chaque logement.",
            "Le temps nécessaire dépend de la taille de la maison et des services demandés, mais en général, cela prend entre 2 et 6 heures.",
            "Oui, nous proposons un nettoyage des vitres à l'intérieur et à l'extérieur, selon vos besoins.",
            "Oui, nous utilisons des produits écologiques pour le nettoyage lorsque cela est possible. Nous privilégions des options respectueuses de l'environnement.",
            "Il n'est pas nécessaire que vous soyez présent. Vous pouvez laisser les clés ou organiser une rencontre préalable.",
            "Oui, nous offrons des réductions pour les clients réguliers ou les nettoyages récurrents.",
            "Vous pouvez réserver un service de nettoyage directement sur notre site web ou par téléphone.",
            "Nous intervenons principalement dans [Nom de la ville/région]. Contactez-nous pour plus d'informations sur la couverture géographique.",
            "Nous effectuons un nettoyage complet de la cuisine, incluant les plans de travail, les appareils, les éviers et les sols.",
            "Oui, nous offrons des services de nettoyage pour les bureaux, avec des options flexibles selon les horaires.",
            "Nous acceptons les paiements par carte bancaire, virement bancaire ou en espèces.",
            "Oui, nous proposons un service de nettoyage d'urgence dans certains cas. Contactez-nous pour plus d'informations.",
            "Si vous n'êtes pas satisfait du nettoyage, contactez-nous immédiatement pour que nous puissions résoudre le problème rapidement."
        ]

        # Insérer les réponses dans la table FAQAnswer
        question_ids = FAQQuestion.query.all()  # Récupérer les questions ajoutées

        for i, answer_text in enumerate(answers):
            question_id = question_ids[i].id  # Associer la réponse à la question correspondante
            new_answer = FAQAnswer(question_id=question_id, answer=answer_text)
            db.session.add(new_answer)

        # Sauvegarder les réponses dans la base de données
        db.session.commit()




# Exécuter les tests
if __name__ == "__main__":
    run_test()
