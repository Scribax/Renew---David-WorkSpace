import unittest
from flask import current_app
from app import create_app
from app.models.cabanas import Cabana

class CabanasTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
    
    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_cabana(self):
        cabana = Cabana()
        cabana.numero = '10'
        cabana.capacidad = '4'
        cabana.nombre = 'sol'
        self.assertTrue(cabana.numero, '10')
        self.assertTrue(cabana.capacidad, '4')
        self.assertTrue(cabana.nombre, 'sol')
    
if __name__ == "__main__":
    unittest.main()
