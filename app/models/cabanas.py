from dataclasses import dataclass
from app import db 

@dataclass
class Cabana(db.Model):
    __tablename__ = 'cabanas'
    id: int = db.Column('id', db.Integer,primary_key=True, autoincrement =True)
    numero: str=db.Column('numero', db.String(50))
    nombre: str=db.Column('nombre',db.String(50))
    capacidad: int = db.Column('capacidad', db.Integer)

