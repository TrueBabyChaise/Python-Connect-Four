import unittest
from src.connectFour import ConnectFour

class ConnectFourTestCase(unittest.TestCase):


	def testResetBoard(self):
		connectF = ConnectFour()
		connectF.addDisc(0, "+")
		connectF.resetBoard()
		for row in connectF._board:
			for case in row:
				self.assertEqual(case, '0')

	def testCreationBoard(self):
		connectF = ConnectFour(1,2)
		self.assertEqual(connectF._nbRow, 1)
		self.assertEqual(connectF._nbColumn, 2)
		self.assertEqual(len(connectF._board), 1)
		for row in connectF._board:
			self.assertEqual(len(row), 2)

	def testAddDiscEmpty(self):
		connectF = ConnectFour()
		connectF.addDisc(0, "+")
		self.assertEqual(connectF._board[connectF._nbRow - 1][0], "+")

	def testAddDiscFull(self):
		connectF = ConnectFour(1)
		connectF.addDisc(0, "+")
		self.assertFalse(connectF.addDisc(0, "+"))
	
	def testAddDiscWrongColumn(self):
		connectF = ConnectFour(1,1)
		self.assertFalse(connectF.addDisc(2, "+"))
	
	def testGetNumberOfDiscInPlay(self):
		connectF = ConnectFour()
		connectF.addDisc(0, "+")
		connectF.addDisc(0, "+")
		connectF.addDisc(0, "+")
		self.assertEqual(connectF.getNumberOfDiscInPlay("+"), 3)

	def testAreDiscAlignedDown(self):
		connectF = ConnectFour()
		connectF.addDisc(0, "+")
		connectF.addDisc(0, "+")
		connectF.addDisc(0, "+")
		connectF.addDisc(0, "+")
		self.assertTrue(connectF.areDiscAligned("+"))
	
	def testAreDiscAlignedRight(self):
		connectF = ConnectFour()
		connectF.addDisc(0, "+")
		connectF.addDisc(1, "+")
		connectF.addDisc(2, "+")
		connectF.addDisc(3, "+")
		self.assertTrue(connectF.areDiscAligned("+"))

	def testAreDiscAlignedUpRight(self):
		connectF = ConnectFour()
		connectF.addDisc(0, "+")
		connectF.addDisc(1, "#")
		connectF.addDisc(1, "+")
		connectF.addDisc(2, "#")
		connectF.addDisc(2, "#")
		connectF.addDisc(2, "+")
		connectF.addDisc(3, "#")
		connectF.addDisc(3, "#")
		connectF.addDisc(3, "#")
		connectF.addDisc(3, "+")
		self.assertTrue(connectF.areDiscAligned("+"))
	
	def testAreDiscAlignedDownRight(self):
		connectF = ConnectFour()
		connectF.addDisc(3, "+")
		connectF.addDisc(2, "#")
		connectF.addDisc(2, "+")
		connectF.addDisc(1, "#")
		connectF.addDisc(1, "#")
		connectF.addDisc(1, "+")
		connectF.addDisc(0, "#")
		connectF.addDisc(0, "#")
		connectF.addDisc(0, "#")
		connectF.addDisc(0, "+")
		self.assertTrue(connectF.areDiscAligned("+"))

def connectFourTestSuite():
	testSuite = unittest.TestSuite()
	return testSuite

if __name__ == '__main__':
    unittest.main()