import os

class Config :
    DEBUG=1

    APP_NAME= "Clean_Service"
    basedir =  os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+ os.path.join(basedir,"cleanService.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "HereIsMySecretkey"

    NO_IMG="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Pas_d%27image_disponible.svg/300px-Pas_d%27image_disponible.svg.png"


    # Configuration pour Flask-Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'christdavidmondjot6@gmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'Davidestceluiquimet5')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', 'christdavidmondjot6@gmail.com')

