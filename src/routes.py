from flask import Blueprint, render_template , request ,send_file
from utils import generate_invoice ,save_to_excel ,send_email
import os

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template("public/index.html")


@bp.route( '/submit_reservation', methods=['POST'] )
def submit_reservation():

    data ={
        "name": request.form['name'],
        "service": request.form['service'],
        "prix": request.form['servicePrix'], 
        "date": request.form['date'],
        "time": request.form['heure'],  
        "adresse": request.form['adresse'],
        "numero": request.form['numero']
        }
    
    # ==== création facture ====
    pdf_path = generate_invoice(data)

    # ==== envoie facture via email ====
    send_email(data,pdf_path)

    # ==== enregistrer sur excel ====
    save_to_excel(data)

    return "Réservation confirmée ! Facture envoyée par email."

@bp.route('/navbar')
def navbar():
    return render_template("layouts/navbar.html")

@bp.route('/bottom')
def bottom():
    return render_template("layouts/bottom.html")

@bp.route('/AboutUS')
def AboutUs():
    return render_template("public/aboutus.html")

@bp.route('/services')
def Services():
    return render_template("public/services.html")

@bp.route('/FAQ')
def Faq():
    return render_template("public/faq.html")

@bp.route('/reservation/horaires')
def Horaire():
    return render_template("public/FSreservation.html")

@bp.route('/reservation/infos')
def Reservation():
    return render_template("public/SSreservation.html")