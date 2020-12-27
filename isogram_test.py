import unittest
from isogram import *

class testIsogram(unittest.TestCase):
    
    def test_blank_File(self):
        self.assertEqual(isogramCounter("blank.txt"), 0)
    def test_upper_and_lower_case_equality(self):
         self.assertEqual(isogramCounter("prueba1.txt"), 1)