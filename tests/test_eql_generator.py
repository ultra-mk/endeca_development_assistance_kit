import unittest
from edak import eql_generator as e


class EQL_GEN_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(EQL_GEN_TEST):
		EQL_GEN_TEST.eql = e.EQL(['Accounting Period', 'GL Date'])


	def test_constant_define_as(self):
		self.assertEqual('Define view_name as SELECT \n', EQL_GEN_TEST.eql.DEFINE_AS)

	def test_EQL_init(self):
		self.assertEqual(['Accounting Period', 'GL Date'], EQL_GEN_TEST.eql.eid_instance_attributes)


	def test_generate_EQL(self):
		self.assertEqual('Define view_name as SELECT \nAccounting Period as "Accounting Period", \nGL Date as "GL Date", \n', EQL_GEN_TEST.eql.generate_EQL())


if __name__ == '__main__':
	unittest.main()