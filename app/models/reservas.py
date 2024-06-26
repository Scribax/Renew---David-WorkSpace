from dataclasses import dataclass
from datetime import datetime
from app import db

@dataclass
class Reserva(db.Model):
    __tablename__ = 'reservas'
    id: int = db.Column('id', db.Integer,primary_key=True, autoincrement =True)
    #apellido: str=db.Column('apelllido',db.String(50))
    fechaini: datetime = db.Column('fechaini', db.DateTime, default=datetime.utcnow, nullable=False)
    fechafin: datetime = db.Column('fechafin', db.DateTime, default=datetime.utcnow, nullable=False)
    
    #cuando tengamos completos los modelos y los esquemas tenemos que incluir esta columna
    #cliente_id = db.Column(db.Integer,db.ForeingKey('cliente.id'))

    # es clientes.id porque se relaciona con _table_name = "clientes" columna id
    # o sea 'clientes.id'
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    cliente = db.relationship("Cliente", foreign_keys=[cliente_id])

    cabana_id = db.Column(db.Integer, db.ForeignKey('cabanas.id'))
    cabana = db.relationship("Cabana", foreign_keys=[cabana_id])



    # pagos_id consideramos que no hace falta porque cada
    # pago está vinculado a un id de reserva
    # pago_id = db.Column(db.Integer, db.ForeingKey('pagos.id'))
