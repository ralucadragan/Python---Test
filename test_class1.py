import unittest
from class1 import Cerc

class Test_cerc(unittest.TestCase):
    # unitest for the Cerc Class

    def setUp(self):
        # create the setUp metod for all 2 parameters
        self.raza1 = 4
        self.raza2 = 7
        self.culoare1 = 'roz'
        self.culoare2 = 'mov'
        self.c1 = Cerc(self.raza1, self.culoare1)
        self.c2 = Cerc(self.raza2, self.culoare2)

    def test_aria(self):
        self.assertEqual(self.c1.aria_cerc(), 50.24)
        self.assertEqual(self.c2.aria_cerc(), 153.00) # gresit

    def test_diametru(self):
        self.assertEqual(self.c1.diametru_cerc(), 9) # gresit
        self.assertEqual(self.c2.diametru_cerc(), 14)

    def test_circumferinta(self):
        self.assertEqual(self.c1.circumferinta_cerc(), 25.12)
        self.assertEqual(self.c2.circumferinta_cerc(), 45) # gresit

if __name__ == '__main__':
    unittest.main