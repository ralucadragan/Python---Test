
from class_formageom import Patrat

class TestClass():
    x = Patrat(5)

    def test_aria_patratului():
        assert Patrat.aria(x) == 25


'''
    def test_perimetrul_patratului():
        assert Patrat.perimetru(5) == 25
        assert Patrat.perimetru(10) == 705

'''