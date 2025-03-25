from flask import Blueprint, render_template , request ,send_file,redirect,url_for
from utils import generate_invoice ,save_to_excel ,send_email
import os
from .dboperations import *

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
   
   
    NUMEROS = get_Numero()
    WHYUS = get_all_WhyUs()
    MESSAGES = get_all_messages()
    SERVICES = getservice()
    return render_template("public/index.html", numeros = NUMEROS , why_us =  WHYUS ,   messages = MESSAGES , services = SERVICES)


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
    # send_email(data,pdf_path)

    # ==== enregistrer sur excel ====
    save_to_excel(data)

    return "Réservation confirmée ! Facture envoyée par email."
    return  redirect(url_for('main.Services'))

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
    SERVICES = getservice()
    return render_template("public/services.html",services = SERVICES)

@bp.route('/FAQ')
def Faq():
    return render_template("public/faq.html")

@bp.route('/reservation/horaires')
def Horaire():
    return render_template("public/FSreservation.html")

@bp.route('/reservation/infos')
def Reservation():
    return render_template("public/SSreservation.html")




# ==================== Partie Admin ====================

@bp.route('/admin/index')
def indexAdmin():
    return render_template("admin/indexAdmin.html")

@bp.route('/admin/navbar')
def NavbarAdmin():
    return render_template("layouts/navbarAdmin.html")

@bp.route('/admin/footer')
def FooterAdmin():
    return render_template("layouts/footerAdmin.html")



# ============  =============
@bp.route('/admin/gestion')
def GestionAdmin():
    return render_template("admin/gestion.html")

@bp.route('/admin/commande')
def CommandeAdmin():
    return render_template("admin/commande.html")

@bp.route('/admin/parametre')
def ParametreAdmin():
    return render_template("admin/parametre.html")