from src import db


class User(db.Model):
    __tablename__ = 'users'  # Assure-toi que le nom de la table est 'users' pour la correspondance avec le ForeignKey
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # Ajouter la relation avec Address
    addresses = db.relationship('Address', back_populates='user')

    def __repr__(self):
        return f"UTILISATEUR : {self.name} - {self.email}"

    


class Address(db.Model):
    __tablename__ = 'addresses'  # Nom de la table explicitement défini

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Assure-toi que 'users.id' est correct
    user = db.relationship("User", back_populates="addresses")

    address = db.Column(db.String(100), nullable=False)  # Augmenter la taille pour l'adresse

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    


