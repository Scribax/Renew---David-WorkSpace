from app.models import Cliente
from marshmallow import validate, fields, Schema, post_load


"""
El atributo dump_only en Marshmallow se utiliza para indicar que un campo debe ser
ignorado durante la deserialización (es decir, durante la conversión de un formato
serializado, como JSON, de vuelta a un objeto Python).
En tu caso, id = fields.Integer(dump_only=True) indica que el campo id no se espera
en los datos entrantes y no se incluirá en los datos salientes.

Por otro lado, el atributo required se utiliza para indicar que un campo debe estar 
presente en los datos entrantes durante la deserialización. Si un campo marcado com
required no está presente en los datos entrantes, Marshmallow generará un error de
validación. En tu caso, numero = fields.String(required=True),
nombre = fields.String(required=True) y
capacidad = fields.Integer(required=True) indican que estos campos deben estar
presentes en los datos entrantes
"""

class ClienteSchema(Schema):
    id = fields.Integer(dump_only=True)
    apellido = fields.String(required=True)
    nombre = fields.String(required=True)
    dni = fields.Integer(required=True)
    # eventualmende podriamos poner en algun ladi una indicacion
    # de que si bien tanto el mail como el telefono no son requeridos
    # son recomendados para tener algun contacto. Hacer como una advertencia
    email= fields.String(required=False)
    telefono = fields.String(required=False)
    direccion = fields.String(required=False)
    provincia= fields.String(required=False)
    ciudad = fields.String(required=False)
    notificaciones = fields.Boolean(required=True)

    @post_load
    def make_cliente(self, data, **kwargs):
        return Cliente(**data)