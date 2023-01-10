'''
4. Folosind TDD, rezolvati urmatoarea problema: Sa se scrie o ierarhie de clase pentru
forme geometrice: FormaGeometrica, Patrat, Dreptunghi, Cerc.
FormaGeometrica este interfata, adice clasa abstracta cu doar metode astracte. Metode:
arie(), perimetru().
Sa se mosteneasca interfata, si sa se implementeze cele 2 metode pentru fiecare din
cele 3 forme geometrice.
'''

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
# FormaGeometrica este interfata, adice clasa abstracta cu doar metode astracte. Metode:
# arie(), perimetru().

    def __init__(self):
        self.pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    @abstractmethod
    def perimetru(self):
        pass

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        FormaGeometrica.__init__(self)
        self.__latura = latura

    def aria(self):
        aria = self.__latura ** 2
        return aria

    def perimetru(self):
        perimetru = self.__latura * 4
        return perimetru

class Dreptunghi(FormaGeometrica):

    def __init__(self, latura1, latura2):
        FormaGeometrica.__init__(self)
        self.__latura1 = latura1
        self.__latura2 = latura2

    def aria(self):
        aria = self.__latura1 * self.__latura2
        return aria

    def perimetru(self):
        perimetru = 2 * (self.__latura1 + self.__latura2)
        return perimetru

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        FormaGeometrica.__init__(self,)
        self.__raza = raza

    def aria(self):
        aria = self.pi * self.__raza ** 2
        return aria

    def perimetru(self):
        perimetru = 2 * self.pi * self.__raza
        return perimetru
