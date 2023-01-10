'''
3.
Clasa Angajat

Atribute: nume, prenume, salariu

Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere_angajat(self):
        print(f'Angajatul se numeste {self.nume} {self.prenume} si are un salar in valaore de {self.salariu} eur.')

    def nume_complet_angajat(self):
        return (self.nume +' ' + self.prenume)

    def salariu_lunar_angajat(self):
        return(self.salariu)

    def salariu_anual(self):
        return(self.salariu *12)

    def marire_salariu_angajat(self):
        procent = 70
        self.salariu = int((procent * self.salariu) / 100) + self.salariu
        return self.salariu
