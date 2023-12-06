import unittest
from src.Model.sueldo_calculo import calcular_sueldo_neto

class TestCalculoSueldoNeto(unittest.TestCase):

    def test_sueldo_sin_horas_extras_ni_tardanzas(self):
        self.assertEqual(calcular_sueldo_neto(2000, 0, 0, 0), 3060)  # Ajusta el resultado esperado

    def test_sueldo_con_horas_extras(self):
        self.assertEqual(calcular_sueldo_neto(2000, 0, 0, 8), 3160)  # Ajusta el resultado esperado

    def test_sueldo_con_tardanzas(self):
        self.assertEqual(calcular_sueldo_neto(2000, 0, 40, 0), 3051.50)  # Ajusta el resultado esperado

    def test_sueldo_con_faltas(self):
        self.assertEqual(calcular_sueldo_neto(2000, 1, 0, 0), 2958)  # Ajusta el resultado esperado

    def test_sueldo_basico_no_numerico(self):
        with self.assertRaises(ValueError):
            calcular_sueldo_neto('dos mil', 0, 0, 0)

    def test_dias_falta_no_numericos(self):
        with self.assertRaises(ValueError):
            calcular_sueldo_neto(2000, 'cero', 0, 0)

    def test_minutos_tardanza_no_numericos(self):
        with self.assertRaises(ValueError):
            calcular_sueldo_neto(2000, 0, 'cero', 0)

    def test_horas_extras_no_numericas(self):
        with self.assertRaises(ValueError):
            calcular_sueldo_neto(2000, 0, 0, 'ocho')

if __name__ == '__main__':
    unittest.main()
