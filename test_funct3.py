import unittest

from funct3 import aria

class TestFunction(unittest.TestCase):

    def test_aria(self):
        self.assertEqual(aria(5,6), 30)
        self.assertEqual(aria(30, 10), 300)
        self.assertEqual(aria(10, 20), 20)

if __name__ == '__main__':
    unittest.main