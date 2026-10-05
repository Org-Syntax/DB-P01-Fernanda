import unittest

from src.suma import sumar


class SumarTests(unittest.TestCase):
    def test_suma_dos_numeros_positivos(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_numeros_negativos(self):
        self.assertEqual(sumar(-2, -3), -5)

    def test_suma_con_cero(self):
        self.assertEqual(sumar(7, 0), 7)


if __name__ == "__main__":
    unittest.main()