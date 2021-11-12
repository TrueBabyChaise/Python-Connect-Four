import unittest
from src.table import Table

class TableTestCase(unittest.TestCase):


	def testGetAllDiscStyle(self):
		table = Table()
		self.assertEqual(table.getAllDiscStyle(), ['#', '%'])

def connectFourTestSuite():
	testSuite = unittest.TestSuite()
	return testSuite

if __name__ == '__main__':
    unittest.main()