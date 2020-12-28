import unittest
from isogram import *

class testIsogram(unittest.TestCase):
    def test_blank_file(self):
        self.assertEqual(isogramCounter("blank.txt"), 0)