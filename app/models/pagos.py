from dataclasses import dataclass
from datetime import datetime
from app import db

@dataclass
class Pago(db.Model):
    __tablename__ = 'pagos'
    id: int = db.Column('id', db.Integer,primary_key=True, autoincrement =True)
    

    #reserva_id: int = db.Column('reserva_id', db.Integer)
    #apellido: str=db.Column('apelllido',db.String(50))
    fechapago: datetime = db.Column('fechapago', db.DateTime, default=datetime.utcnow, nullable=False)
    # los montos los guardamos en centavos y para mostrarlos
    # o hacer algun calclo hay que dividirlo por cien
    monto: int=db.Column('monto', db.Integer)
    tipopago: str=db.Column('tipopago',db.String(50), nullable=False)

    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.id'))
    reserva = db.relationship("Reserva", foreign_keys=[reserva_id]) 

