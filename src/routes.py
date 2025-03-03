from flask import Blueprint, render_template


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template("public/index.html")

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