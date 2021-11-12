#!/usr/bin/env python3

from unittest import runner
from src.connectFour import ConnectFour
from src.player import Player
from tests.testPlayer import playerTestSuite
import unittest

class BasicTestCase(unittest.TestCase):

	def testOneEqualOne(self):
		self.assertEqual(1, 1)

def main():
	runner = unittest.TextTestRunner()
	runner.run(playerTestSuite())
	
if __name__ == '__main__':
	unittest.main()