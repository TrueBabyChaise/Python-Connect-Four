import unittest
from src.player import Player

class PlayerTestCase(unittest.TestCase):

	def testChangeNameTest(self):
		p = Player('%')
		p.name = "Test"
		self.assertEqual(p.name, "Test")

	def testGetDiscStyle(self):
		p = Player('%')
		self.assertEqual(p.discStyle, '%')

def playerTestSuite():
	testSuite = unittest.TestSuite()
	testSuite.addTest(PlayerTestCase('testChangeNameTest'))
	testSuite.addTest(PlayerTestCase('testGetDiscStyle'))
	return testSuite

if __name__ == '__main__':
    unittest.main()