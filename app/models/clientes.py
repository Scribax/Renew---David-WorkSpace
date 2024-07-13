from dataclasses import dataclass
from app import db 

@dataclass
class Cliente(db.Model):
    __tablename__ = 'clientes'
    id: int = db.Column('id', db.Integer,primary_key=True, autoincrement =True)
    apellido: str=db.Column('apelllido',db.String(50))
    nombre: str=db.Column('nombre', db.String(50))
    dni: int = db.Column('dni', db.Integer)
    email: str=db.Column('email',db.String(50))
    telefono: str=db.Column('telefono',db.String(15))
    direcccion = str=db.Column('direccion',db.String(50))
    # por ahora no le vamos a guardar un passwor de cliente
    # password = str=db.Column('password',db.String(64)) # un hash varia entre 224 y 512 bits
    provincia: str=db.Column('provincia',db.String(50))
    ciudad: str=db.Column('ciudad', db.String(50))
    notificaciones: bool=db.Column('notificaciones',db.Boolean())


