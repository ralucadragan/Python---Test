import unittest

from funct1 import string

class TestFunction(unittest.TestCase):

    def test_char(self):
        self.assertTrue(string('m'))
        self.assertTrue(string('e'))
        self.assertTrue(string('x'))
        self.assertFalse(string('x'))

if __name__ == '__main__':
    unittest.main

