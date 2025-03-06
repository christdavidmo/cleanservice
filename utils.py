from flask_mail import Message
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
import os
from datetime import datetime
from src import mail 

def generate_invoice(data):
    """ Génère un fichier PDF avec les informations de réservation """
    # Définir le chemin vers le répertoire factures dans src
    directory = os.path.join(os.path.dirname(__file__), 'factures')
    # Assurez-vous que le répertoire existe
    os.makedirs(directory, exist_ok=True)
    # Définir le chemin complet du fichier PDF
    facture_path = os.path.join(directory, f"{data['name']}_facture.pdf")

    c = canvas.Canvas(facture_path, pagesize=letter)
    c.drawString(100, 750, f"Facture pour {data['name']}")
    c.drawString(100, 730, f"Service : {data['service']}")
    c.drawString(100, 710, f"Date : {data['date']}")
    c.drawString(100, 690, f"Heure : {data['time']}")
    c.drawString(100, 670, f"Prix : {data['prix']} FCFA")
    c.drawString(100, 650, f"Adresse : {data['adresse']}")
    c.drawString(100, 630, f"Téléphone : {data['numero']}")

    c.save()
    return facture_path

# def send_email(data, pdf_path):
#     """ Envoie un email avec la facture en pièce jointe """
#     msg = Message("Votre Facture", recipients=[data['adresse']])
#     msg.body = f"""
#     Bonjour {data['name']},

#     Merci d'avoir réservé notre service "{data['service']}".

#     Détails :
#     - Date : {data['date']}
#     - Heure : {data['time']}
#     - Prix : {data['prix']} FCFA

#     Vous trouverez votre facture en pièce jointe.

#     Cordialement,
#     L'équipe de nettoyage
#     """
#     with open(pdf_path, "rb") as pdf:
#         msg.attach("facture.pdf", "application/pdf", pdf.read())

#     mail.send(msg)


def send_email(data, pdf_path):
    msg = Message("Votre Facture", recipients=[data['adresse']])
    msg.body = f"Bonjour {data['name']},\n\nVoici votre facture pour le service {data['service']}.\n\nMerci !"

    with open(pdf_path, "rb") as f:
        msg.attach("facture.pdf", "application/pdf", f.read())

    mail.send(msg)  #  Envoi de l'email


def save_to_excel(data):
    """ Sauvegarde les données dans un fichier Excel mensuel """
    mois = datetime.now().strftime("%Y-%m")
    # Définir le chemin vers le répertoire src
    directory = os.path.join(os.path.dirname(__file__), 'src')
    # Assurez-vous que le répertoire existe
    os.makedirs(directory, exist_ok=True)
    # Définir le nom complet du fichier avec le chemin
    filename = os.path.join(directory, f"reservations_{mois}.xlsx")

    # Vérifier si le fichier existe
    if os.path.exists(filename):
        df = pd.read_excel(filename)
    else:
        df = pd.DataFrame(columns=["Nom", "Service", "Date", "Heure", "Prix", "Adresse", "Téléphone"])

    # Ajouter la nouvelle réservation
    new_data = pd.DataFrame([data])
    df = pd.concat([df, new_data], ignore_index=True)

    # Sauvegarder dans Excel
    df.to_excel(filename, index=False)
