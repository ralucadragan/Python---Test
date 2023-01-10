import unittest

from funct2 import sum

class TestFunction(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sum(8), 36)
        self.assertEqual(sum(3), 6)
        self.assertEqual(sum(5), 10)

if __name__ == '__main__':
    unittest.main