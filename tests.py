import unittest
from algorithms import *

class Test(unittest.TestCase):

	def setUp(self):
		self.setup1 = [ 5, 3, 0, 4, 1, 2 ]

	def tearDown(self):
		del( self.setup1 )

	def test_bubble(self):
		bubble_sort( self.setup1 )
		self.assertTrue( self.setup1 == [ 0, 1, 2, 3, 4, 5 ] )

	def test_selection(self):
		selection_sort( self.setup1 )
		self.assertTrue( self.setup1 == [ 0, 1, 2, 3, 4, 5 ] )

if __name__ == '__main__':
	unittest.main()
