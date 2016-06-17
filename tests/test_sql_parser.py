import unittest
from edak import sql_parser as sp

class SQL_PARSER_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(SQL_PARSER_TEST):
		SQL_PARSER_TEST.sp = sp.SQL_PARSER('QTO_308.sql')

	def test_is_this_thing_on(self):
		self.assertEqual(['1','2','3'], SQL_PARSER_TEST.sp.column_names)

#this test is returning true no matter what.
	def test_check_for_file(self):
		self.assertTrue(SQL_PARSER_TEST.sp.check_for_file)

