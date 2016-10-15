from unittest import TestCase
from Calculadora import *


#Tests unitarios
class TestCalculadora(TestCase):

    def setUp(self):
        self.objeto = Calculadora('',8, 4)

    def tearDown(self):
        del self.objeto

    def test_suma(self):
        self.assertEqual(Calculadora.suma(self.objeto), 12)

    def test_resta(self):
        self.assertEqual(Calculadora.resta(self.objeto), 4)

    def test_multiplicacion(self):
        self.assertEqual(Calculadora.multiplicacion(self.objeto), 32)

    def test_division(self):
        self.assertEqual(Calculadora.division(self.objeto), 2)
