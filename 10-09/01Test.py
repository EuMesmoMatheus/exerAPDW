
import unittest
from _01 import  randomGeneric

class TestGerarArrayAleatorio(unittest.TestCase):

    def randomGeneric(self):
        array =  randomGeneric()
        self.randomGeneric(len(array), 20000)

    def randomGeneric(self):
        array =  randomGeneric()
        for valor in array:
            self.assertGreaterEqual(valor, -999999)
            self.assertLessEqual(valor, 999999)

if __name__ == '__main__':
    unittest.main()
