import os

class Config :
    DEBUG=1
    SQLALCHEMY_ECHO = True


    APP_NAME= "Clean_Service"
    basedir =  os.path.abspath(os.path.dirname(__file__))

  
    SQLALCHEMY_DATABASE_URI = "postgresql://cleanservicedb_user:12ZIxEnc3Qqa8bUpBUApfHuaKe1TXNY4@dpg-cv8489tds78s73cso6k0-a/cleanservicedb"
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost:5432/cleanServiceDb"



    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "HereIsMySecretkey"

    NO_IMG="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Pas_d%27image_disponible.svg/300px-Pas_d%27image_disponible.svg.png"


    # Configuration pour Flask-Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', '')




  # SQLALCHEMY_DATABASE_URI = "sqlite:///"+ os.path.join(basedir,"cleanService.sqlite")
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://")




   # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://cleanservicedb_user:12ZIxEnc3Qqa8bUpBUApfHuaKe1TXNY4@dpg-cv8489tds78s73cso6k0-a/cleanservicedb').replace("postgres://", "postgresql://")

    # if not SQLALCHEMY_DATABASE_URI:
    #     raise ValueError("DATABASE_URL n'est pas défini. Configure une base PostgreSQL sur Render.")

