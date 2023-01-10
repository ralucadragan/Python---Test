import unittest
from class2 import Angajat

class Test_Angajat(unittest.TestCase):

    def setUp(self):
        self.nume1 = 'Dragan'
        self.nume2 = 'Berenyi'
        self.prenume1 = 'Raluca'
        self.prenume2 = 'Stefania'
        self.salar1 = 3000
        self.salar2 = 7000
        self.a1 = Angajat(self.nume1, self.prenume1, self.salar1)
        self.a2 = Angajat(self.nume2, self.prenume2, self.salar2)


    def test_numecomplet(self):
        self.assertTrue(self.a1.nume_complet_angajat() == self.nume1 + ' ' + self.prenume1)
        self.assertEqual(self.a2.nume_complet_angajat(), 'Berenyi Stefan') #fail

    def test_salariulunar(self):
        self.assertEqual(self.a1.salariu_lunar_angajat(), 3000)
        self.assertEqual(self.a2.salariu_lunar_angajat(), 6000) #fail

    def test_salariuanual(self):
        self.assertEqual(self.a1.salariu_anual(), 36000)
        self.assertEqual(self.a2.salariu_anual(), 84500) #fail

    def test_mariresalariu(self):
        self.assertEqual(self.a1.marire_salariu_angajat(), 5700) #fail
        self.assertEqual(self.a2.marire_salariu_angajat(), 9100)

if __name__ == '__main__':
    unittest.main

