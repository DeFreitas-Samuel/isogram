import unittest
from isogram import *

class testIsogram(unittest.TestCase):
    def testBlankFile(self):
        self.assertEqual(isogramCounter("blank.txt"),0)