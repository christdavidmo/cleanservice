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
    us = get_about_us_content()
    return render_template("public/aboutus.html",conts = us )

@bp.route('/services')
def Services():
    SERV_CONTENT = get_all_service_content()
    SERVICES = getservice()
    return render_template("public/services.html",servcontents = SERV_CONTENT ,services = SERVICES)

@bp.route('/FAQ')
def Faq():
    QANDA = getQuestion_frequently()
    return render_template("public/faq.html",qanda = QANDA)

@bp.route('/reservation/horaires')
def Horaire():
    return render_template("public/FSreservation.html")

@bp.route('/reservation/infos')
def Reservation():
    return render_template("public/SSreservation.html")




# ====================  ====================
#               Partie Admin
# ====================  ====================


@bp.route('/admin/index')
def indexAdmin():
    return render_template("admin/indexAdmin.html")

@bp.route('/admin/navbar')
def NavbarAdmin():
    return render_template("layouts/navbarAdmin.html")

@bp.route('/admin/footer')
def FooterAdmin():
    return render_template("layouts/footerAdmin.html")



# ============  GESTION =============
@bp.route('/admin/gestion')
def GestionAdmin():
    return render_template("admin/gestion.html")

@bp.route('/admin/gestion/details')
def GestionDetailsAdmin():
    SERVICES = getservice()
    return render_template("admin/gestionnDetails.html" , services =  SERVICES )

@bp.route('/admin/gestion/details/service/modifier', methods=['POST'])
def modifier_service():
    ID = request.form.get('id')
    NOM = request.form.get('nameService')
    PRIX = request.form.get('priceService')

    service = find_service_by_id(ID)
    modification_service(service,NOM,PRIX)
    return redirect(url_for('main.GestionDetailsAdmin'))

@bp.route('/admin/gestion/service/supprimer', methods=['POST'])
def suppression_service():
    ID = request.form.get(id)
    service = find_service_by_id(ID)
    supprimer_service(service)
    return redirect(url_for('main.GestionDetailsAdmin'))


@bp.route('/admin/faq/modifier-reponse', methods=['POST'])
def modifier_reponse():
    ANSWER_ID = request.form.get('answer_id')
    NEW_REPONSE = request.form.get('new_reponse')

    answer = FAQAnswer.query.get(ANSWER_ID)
    if answer:
        answer.answer = NEW_REPONSE
        db.session.commit()
    return redirect(url_for('main.gestion_faq'))


@bp.route('/admin/faq/ajouter-reponse', methods=['POST'])
def ajouter_reponse():
    question_id = request.form.get('question_id')
    answer_text = request.form.get('new_answer')

    question = FAQQuestion.query.get(question_id)
    if question and answer_text:
        nouvelle_reponse = FAQAnswer(
            question_id=question.id,
            answer=answer_text
        )
        db.session.add(nouvelle_reponse)
        db.session.commit()

    return redirect(url_for('main.gestion_faq'))




@bp.route('/admin/gestion/faq')
def gestion_faq():
    QUESTIONS = get_All_Faq()
    return render_template('admin/gestionFaqDetails.html', questions = QUESTIONS)











@bp.route('/admin/dashboard')
def dashboard_admin():
    return render_template('admin/dashboard.html')


# ============  GESTION =============



@bp.route('/admin/commande')
def CommandeAdmin():
    return render_template("admin/commande.html")

@bp.route('/admin/parametre')
def ParametreAdmin():
    return render_template("admin/parametre.html")


# ====================  ====================
#               Partie Admin
# ====================  ====================




# ======================= POURQUOI NOUS  =======================
@bp.route('/admin/gestion/why-us')
def gestion_why_us():
    reasons = WhyUs.query.all()
    return render_template('admin/content/gestion_why_us.html', reasons=reasons)

@bp.route('/admin/why-us/ajouter', methods=['POST'])
def ajouter_why_us():
    reason = request.form.get('reason')
    if reason:
        new_reason = WhyUs(reason=reason)
        db.session.add(new_reason)
        db.session.commit()
    return redirect(url_for('main.gestion_content'))

@bp.route('/admin/why-us/modifier', methods=['POST'])
def modifier_why_us():
    id = request.form.get('id')
    reason = request.form.get('reason')
    entry = WhyUs.query.get(id)
    if entry and reason:
        entry.reason = reason
        db.session.commit()
    return redirect(url_for('main.gestion_content'))

@bp.route('/admin/why-us/supprimer/<int:id>', methods=['POST'])
def supprimer_why_us(id):
    RAISON = find_Why_Us(id)
    if RAISON:
       delete_Why_Us(RAISON.id)
    return redirect(url_for('main.gestion_content'))
# ======================= POURQUOI NOUS  =======================



# ======================= MESSAGE =======================
@bp.route('/admin/gestion/messages')
def gestion_messages():
    messages = get_all_messages()
    return render_template('admin/content/gestion_messages.html', messages=messages)

@bp.route('/admin/messages/ajouter', methods=['POST'])
def ajouter_message():
    content = request.form.get('content')
    if content:
        addMessage(content)
    return redirect(url_for('main.gestion_messages'))

@bp.route('/admin/messages/supprimer/<int:message_id>', methods=['POST'])
def supprimer_message(message_id):
    delete_message(message_id)
    return redirect(url_for('main.gestion_messages'))

@bp.route('/admin/messages/modifier', methods=['POST'])
def modifier_message():
    message_id = request.form.get('message_id')
    new_content = request.form.get('new_content')
    update_message(message_id, new_content)
    return redirect(url_for('main.gestion_messages'))

# ======================= MESSAGE =======================



# ======================= ABOUT US CONTENT =======================
@bp.route('/admin/gestion/about-us')
def gestion_about_us():
    paragraphs = get_about_us_content()
    return render_template('admin/content/gestion_about_us.html', paragraphs=paragraphs)


@bp.route('/admin/about-us/ajouter', methods=['POST'])
def ajouter_about_us():
    paragraph = request.form.get('paragraph')
    if paragraph:
        add_about_us(paragraph)
    return redirect(url_for('main.gestion_about_us'))

@bp.route('/admin/about-us/modifier', methods=['POST'])
def modifier_about_us():
    ID = request.form.get('id')
    paragraph = request.form.get('paragraph')
    update_about_us(ID, paragraph)
    return redirect(url_for('main.gestion_about_us'))

@bp.route('/admin/about-us/supprimer/<int:id>', methods=['POST'])
def supprimer_about_us(id):
    delete_about_us(id)
    return redirect(url_for('main.gestion_about_us'))

# ======================= ABOUT US CONTENT  =======================



# ======================= SERVICE CONTENT  =======================
@bp.route('/admin/gestion/service-content')
def gestion_service_content():
    services = get_all_service_content()
    return render_template('admin/content/gestion_service_content.html', services=services)


@bp.route('/admin/service/ajouter', methods=['POST'])
def ajouter_service_content():
    paragraph = request.form.get('paragraph')
    if paragraph:
        add_service_content(paragraph)
    return redirect(url_for('main.gestion_service_content'))

@bp.route('/admin/service/modifier', methods=['POST'])
def modifier_service_content():
    ID = request.form.get('id')
    paragraph = request.form.get('paragraph')
    update_service_content(ID, paragraph)
    return redirect(url_for('main.gestion_service_content'))

@bp.route('/admin/service/supprimer/<int:id>', methods=['POST'])
def supprimer_service_content(id):
    delete_service_content(id)
    return redirect(url_for('main.gestion_service_content'))

# ======================= SERVICE CONTENT  =======================



# ======================= INFORMATIONS  =======================
@bp.route('/admin/gestion/informations')
def gestion_informations():
    infos = Information.query.all()
    return render_template('admin/content/gestion_informations.html', informations=infos)
# ======================= INFORMATIONS =======================


# ======================= TELEPHONE  =======================
@bp.route('/admin/gestion/telephones')
def gestion_telephones():
    telephones = Telephone.query.all()
    return render_template('admin/content/gestion_telephones.html', telephones=telephones)

# Route pour ajouter un numéro
@bp.route('/admin/ajouter/numero', methods=['POST'])
def ajouter_numero():
    numero = request.form['numero']
    business_id = request.form['business_id']  # On suppose que tu passes un `business_id` depuis le formulaire
    add_numero(numero, business_id)
    return redirect(url_for('main.gestion_telephones'))

# Route pour supprimer un numéro
@bp.route('/admin/supprimer/numero/<int:id>', methods=['GET'])
def supprimer_numero(id):
    Delete_Numero(id)
    return redirect(url_for('main.gestion_telephones'))
# ======================= TELEPHONE  =======================













# ==============================================

# Route pour afficher la gestion des horaires d'ouverture
@bp.route('/admin/gestion/ouvertures')
def gestion_ouvertures():
    horaires = Ouverture.query.all()
    return render_template('admin/content/gestion_ouvertures.html', horaires=horaires)

# Route pour ajouter un horaire d'ouverture
@bp.route('/admin/ajouter/ouverture', methods=['POST'])
def ajouter_ouverture():
    jour = request.form['jour']
    heure_ouverture = request.form['heure_ouverture']
    heure_fermeture = request.form['heure_fermeture']

    add_ouverture(jour, heure_ouverture, heure_fermeture)
    return redirect(url_for('main.gestion_ouvertures'))

# Route pour mettre à jour un horaire
@bp.route('/admin/modifier/ouverture/<int:id>', methods=['POST'])
def modifier_ouverture(id):
    jour = request.form['jour']
    heure_ouverture = request.form['heure_ouverture']
    heure_fermeture = request.form['heure_fermeture']

    update_ouverture(id, jour, heure_ouverture, heure_fermeture)
    return redirect(url_for('main.gestion_ouvertures'))

# Route pour supprimer un horaire
@bp.route('/admin/supprimer/ouverture/<int:id>', methods=['GET'])
def supprimer_ouverture(id):
    delete_ouverture(id)
    return redirect(url_for('main.gestion_ouvertures'))

# ==============================================



# =========== RESEAUX ===================
@bp.route('/admin/gestion/reseaux')
def gestion_reseaux():
    reseaux = Reseau.query.all()
    return render_template('admin/content/gestion_reseaux.html', reseaux=reseaux)

# Route pour afficher tous les liens des réseaux sociaux
# @bp.route('/admin/gestion/reseaux')
# def gestion_reseaux():
#     reseaux = get_all_reseaux()  # Récupère tous les liens des réseaux sociaux
#     return render_template('admin/gestionReseaux.html', reseaux=reseaux)

# Route pour ajouter un lien de réseau social
@bp.route('/admin/ajouter/reseau', methods=['POST'])
def ajouter_reseau():
    lien = request.form['lien']
    add_reseau(lien)
    return redirect(url_for('main.gestion_reseaux'))

# Route pour supprimer un lien de réseau social
@bp.route('/admin/supprimer/reseau/<int:id>', methods=['GET'])
def supprimer_reseau(id):
    delete_reseau(id)
    return redirect(url_for('main.gestion_reseaux'))
# =========== RESEAUX ===================


# @bp.route('/admin/gestion/home-text')
# def gestion_home_text():
#     textes = HomeText.query.all()  # Crée ce modèle si non existant
#     return render_template('admin/gestion_home_text.html', textes=textes)
# @bp.route('/admin/gestion/carousel')
# def gestion_carousel():
#     carousels = Carousel.query.all()  # Crée ce modèle si non existant
#     return render_template('admin/gestion_carousel.html', carousels=carousels)
