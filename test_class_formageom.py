import unittest
from class_formageom import Patrat, Dreptunghi, Cerc

class Test_Patrat(unittest.TestCase):
    def setUp(self):
        self.latura1 = 5
        self.latura2 = 30
        self.p1 = Patrat(self.latura1)
        self.p2 = Patrat(self.latura2)

    def test_aria_patrat(self):
        self.assertEqual(self.p1.aria(), 25)
        self.assertEqual(self.p2.aria(), 75) # fail -> 900

    def test_perimetru_patrat(self):
        self.assertEqual(self.p1.perimetru(), 25) # fail -> 20
        self.assertEqual(self.p1.perimetru(), 20)
        self.assertEqual(self.p2.perimetru(), 120)

class Test_Dreptunghi(unittest.TestCase):
    def setUp(self):
        self.latura1 = 5
        self.latura2 = 30
        self.latura3 = 10
        self.latura4 = 50
        self.d1 = Dreptunghi(self.latura1, self.latura2)
        self.d2 = Dreptunghi(self.latura3, self.latura4)

    def test_aria_dreptunghi(self):
        self.assertEqual(self.d1.aria(), 75) # fail -> 150
        self.assertEqual(self.d1.aria(), 150)
        self.assertEqual(self.d2.aria(), 1005)
        self.assertEqual(self.d2.aria(), 500)

    def test_perimetru_dreptunghi(self):
        self.assertEqual(self.d1.perimetru(), 150) #fail ->70
        self.assertEqual(self.d2.perimetru(), 150)  # fail ->120

class Test_Cerc(unittest.TestCase):
    def setUp(self):
        self.raza1 = 10
        self.raza2 = 15
        self.c1 = Cerc(self.raza1)
        self.c2 = Cerc(self.raza2)

    def test_aria_cercului(self):
        self.assertEqual(self.c1.aria(), 314)
        self.assertEqual(self.c2.aria(), 705) # fail -> 706.5

    def test_perimetrul_cercului(self):
        self.assertEqual(self.c1.perimetru(), 70) # fail -> 62.800000000000004
        self.assertEqual(self.c2.perimetru(), 94.20)

if __name__ == '__main__':
    unittest.main