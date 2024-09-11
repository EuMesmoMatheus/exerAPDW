import unittest
from _03 import converter_massa_lunar, converter_massa_marte

class TestConversaoUnidadesEspaciais(unittest.TestCase):

    def test_converter_massa_lunar(self):
        # Testando a conversão para a massa lunar
        self.assertEqual(converter_massa_lunar(6), 1)  # 6 kg na Terra = 1 kg na Lua
        self.assertEqual(converter_massa_lunar(12), 2)  # 12 kg na Terra = 2 kg na Lua
        self.assertEqual(converter_massa_lunar(0), 0)   # 0 kg na Terra = 0 kg na Lua
        self.assertAlmostEqual(converter_massa_lunar(7.5), 1.25)  # 7.5 kg na Terra = 1.25 kg na Lua

    def test_converter_massa_marte(self):
        # Testando a conversão para a massa em Marte
        massa_terrestre = 10
        resultado_esperado = (9.81 / 3.71) * massa_terrestre
        self.assertAlmostEqual(converter_massa_marte(massa_terrestre), resultado_esperado)
        
        massa_terrestre = 20
        resultado_esperado = (9.81 / 3.71) * massa_terrestre
        self.assertAlmostEqual(converter_massa_marte(massa_terrestre), resultado_esperado)
        
        self.assertEqual(converter_massa_marte(0), 0)  # 0 kg na Terra = 0 kg em Marte
        self.assertAlmostEqual(converter_massa_marte(15), (9.81 / 3.71) * 15)

if __name__ == '__main__':
    unittest.main()
