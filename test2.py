from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://cleanservicedb_user:12ZIxEnc3Qqa8bUpBUApfHuaKe1TXNY4@dpg-cv8489tds78s73cso6k0-a.oregon-postgres.render.com/cleanservicedb"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("✅ Connexion réussie à la BD Render !")
except Exception as e:
    print("❌ Erreur de connexion :", e)
