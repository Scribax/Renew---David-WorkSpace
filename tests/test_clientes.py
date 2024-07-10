import unittest
from flask import current_app
from app import create_app
from app.models.clientes import Cliente

class ClientesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        

        
        
        
    def test_Cliente(self):    
        cliente = Cliente()
        cliente.apellido = 'Martinez'
        cliente.ciudad = "Mendoza"
        cliente.direccion = "Lavalle"
        cliente.email = "nombre@servidor.com"
        self.assertTrue(cliente.apellido, 'Martinez')
        self.assertTrue(cliente.ciudad, 'Mendoza')
        self.assertTrue(cliente.direccion,"Lavalle")
        self.assertTrue(cliente.email) 