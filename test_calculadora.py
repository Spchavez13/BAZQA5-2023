import unittest
from calculadora import Calculadora, ErrorAlDividirEntreCero


class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        calcu = Calculadora()
        resultado = calcu.sumar(1, 3)
        self.assertEqual(resultado, 4)

    def test_sumar_3_y5_regresa_8(self):
        calcu = Calculadora()
        resultado = calcu.sumar(3, 5)
        self.assertEqual(resultado, 8)

    def test_restar_8_y_2_regresa_6(self):
        calcu = Calculadora()
        resultado = calcu.restar(8, 2)
        self.assertEqual(resultado, 6)

    def test_restar_5_y_5_regresa_0(self):
        calcu = Calculadora()
        resultado = calcu.restar(5, 5)
        self.assertEqual(resultado, 0)

    def test_dividir_5_y_5_regresa_1(self):
        calcu = Calculadora()
        resultado = calcu.restar(5, 5)
        self.assertEqual(resultado, 0)

    def test_restar_10_y_0_regresa_mensaje_error(self):
        calcu = Calculadora()
        with self.assertRaises(ErrorAlDividirEntreCero):
            resultado = calcu.dividir(10, 0)
