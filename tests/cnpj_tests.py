import sys
sys.path.insert(0,'..')
import unittest
import cnpj

class CNPJTests(unittest.TestCase):
	"""docstring for CNPJTests"""
	def setUp(self):
		self.valid_cnpj = '11444777000161'
		self.invalid_cnpj = '11444777000162'

	def test_validate_cnpj_true(self):
		self.assertTrue(cnpj.validate(self.valid_cnpj))

	def test_validate_cnpj_false(self):
		self.assertFalse(cnpj.validate(self.invalid_cnpj))

if __name__ == '__main__':
    unittest.main(verbosity=2)