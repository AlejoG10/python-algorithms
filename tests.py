import unittest
from algorithms import *

class Test(unittest.TestCase):

	def setUp(self):
		self.setup1 = [ 5, 3, 0, 4, 1, 2 ]
		self.setup2 = [ -10, 5, 15, -5, -15, 10 ]

	def tearDown(self):
		del( self.setup1 )
		del( self.setup2 )

	def test_bubble(self):
		bubble_sort( self.setup1 )
		self.assertTrue( self.setup1 == [ 0, 1, 2, 3, 4, 5 ] )

	def test_selection(self):
		selection_sort( self.setup2 )
		self.assertTrue( self.setup2 == [ -15, -10, -5, 5, 10, 15 ] )

if __name__ == '__main__':
	unittest.main()
