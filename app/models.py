from app.database import db

class Certificado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    curso = db.Column(db.String(100), nullable=False)
    data_emissao = db.Column(db.Date, nullable=False)
