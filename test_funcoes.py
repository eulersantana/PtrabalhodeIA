import unittest
from funcoes import *


class testa_funcoes(unittest.TestCase):
	def test_geraTabuleiro(self):
		self.assertEqual(geraTabuleiro()[0].cor,'preto')



if __name__ == '__main__':
    unittest.main()