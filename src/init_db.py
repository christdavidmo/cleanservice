from app import create_app
from extensions import db  # adapte si `db` est ailleurs

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Tables créées avec succès dans la base de données PostgreSQL !")
