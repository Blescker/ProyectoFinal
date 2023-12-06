import unittest
from src.Model.sueldo_calculo import calcular_sueldo_neto

class TestCalculoSueldoNeto(unittest.TestCase):

    def test_sueldo_sin_horas_extras_ni_tardanzas(self):
        # Testear el cálculo del sueldo neto sin horas extras ni tardanzas
        self.assertEqual(calcular_sueldo_neto(2000, 0, 0, 0), 3060)  # Ajusta el resultado esperado

    def test_sueldo_con_horas_extras(self):
        # Testear el cálculo con horas extras
        self.assertEqual(calcular_sueldo_neto(2000, 0, 0, 8), 3160)  # Ajusta el resultado esperado

    def test_sueldo_con_tardanzas(self):
        # Testear el cálculo con tardanzas
        self.assertEqual(calcular_sueldo_neto(2000, 0, 40, 0), 3051.50)  # Ajusta el resultado esperado

    def test_sueldo_con_faltas(self):
        # Testear el cálculo con días de faltas
        self.assertEqual(calcular_sueldo_neto(2000, 1, 0, 0), 2958)  # Ajusta el resultado esperado

    # Puedes añadir más tests para diferentes combinaciones de entradas

if __name__ == '__main__':
    unittest.main()
