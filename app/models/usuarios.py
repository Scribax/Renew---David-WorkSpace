from dataclasses import dataclass
from app import db 

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id: int = db.Column('id', db.Integer,primary_key=True, autoincrement =True)
    apellido: str=db.Column('apelllido',db.String(50))
    nombre: str=db.Column('nombre', db.String(50))
    dni: int = db.Column('dni', db.Integer)
    email: str=db.Column('email',db.String(50))
    telefono: str=db.Column('telefono',db.String(15))
    direcccion = str=db.Column('direccion',db.String(50))
    password = str=db.Column('password',db.String(64)) # un hash varia entre 224 y 512 bits
