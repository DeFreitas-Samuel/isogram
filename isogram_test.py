import unittest
from isogram import *

class testIsogram(unittest.TestCase):
    def testBlankFile(self):
        self.assertEqual(isogramCounter("blank.txt"),0)
    
    def testUpperCaseAndLowerCaseAreEqual(self):
        self.assertEqual(isogramCounter("Prueba1.txt"),1)
    
    def testIsogramList(self):
        self.assertEqual(isogramCounter("Isogram list.txt"),4376)