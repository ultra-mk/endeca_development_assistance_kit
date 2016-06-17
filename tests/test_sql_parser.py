import unittest
from edak import sql_parser as sp

class SQL_PARSER_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(SQL_PARSER_TEST):
		SQL_PARSER_TEST.instance = sp.SQL_PARSER('QTO_308.sql')
		SQL_PARSER_TEST.sql_lines = SQL_PARSER_TEST.instance.open_file()
		SQL_PARSER_TEST.column_headers = SQL_PARSER_TEST.instance.get_selected_columns(SQL_PARSER_TEST.sql_lines, 34)


	def test_check_for_file(self):
		self.assertTrue(SQL_PARSER_TEST.instance.check_for_file())


	def test_open_file(self):
		self.assertEqual('SELECT', SQL_PARSER_TEST.instance.open_file()[0])


	def test_find_from_index(self):
		self.assertEqual(37, SQL_PARSER_TEST.instance.find_from_index(SQL_PARSER_TEST.sql_lines))


	def test_get_select_columns(self):
		self.assertEqual(24, 
			len(SQL_PARSER_TEST.instance.get_selected_columns(SQL_PARSER_TEST.sql_lines, 34)))

	def test_remove_table_names(self):
		self.assertEqual('CUSTOMER_TRX_ID', SQL_PARSER_TEST.instance.remove_table_names(SQL_PARSER_TEST.column_headers)[0])


	def test_remove_table_names_len(self):
		self.assertEqual(24,len(SQL_PARSER_TEST.instance.remove_table_names(SQL_PARSER_TEST.column_headers)))
