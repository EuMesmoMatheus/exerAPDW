import unittest
from _02 import randomGeneric, vetorOrder

class TestOrdenacao(unittest.TestCase):

    def test_tamanho_do_array(self):
        array = randomGeneric()
        self.assertEqual(len(array), 20000)

    def test_valores_no_intervalo(self):
        array = randomGeneric()
        for valor in array:
            self.assertGreaterEqual(valor, -999999)
            self.assertLessEqual(valor, 999999)

    def test_ordenacao_correta(self):
        array = randomGeneric()
        sorted_array = vetorOrder(array.copy()) 

    def test_vetor_ja_ordenado(self):
        array = list(range(-10, 11))  
        sorted_array = vetorOrder(array.copy())  
        self.assertEqual(sorted_array, array)

if __name__ == '__main__':
    unittest.main()
