import unittest
from isogram import *

class testIsogram(unittest.TestCase):
    def test_blank_file(self):
        self.assertEqual(isogramCounter("blank.txt"), 0)

    def test_equality_of_lower_and_upper_case(self):
        self.assertEqual(isogramCounter("prueba1.txt"), 0)

    def test_isogram_list(self):
        self.assertEqual(isogramCounter("isogram list.txt"), 4376)