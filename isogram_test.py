import unittest
from isogram import *

class testIsogram(unittest.TestCase):
    def blankFile(self):
        self.assertEqual(isogramCounter("blank.txt"), 0)