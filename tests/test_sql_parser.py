import unittest
from edak import sql_parser as sp
from edak import utils


class SQL_PARSER_TEST(unittest.TestCase):

    @classmethod
    def setUpClass(SQL_PARSER_TEST):
        SQL_PARSER_TEST.instance = sp.SQL_PARSER('sql_parser_test_doc.sql')
        SQL_PARSER_TEST.sql_lines = utils.open_file_split_into_lines('sql_parser_test_doc.sql')
        SQL_PARSER_TEST.column_headers = SQL_PARSER_TEST.instance.get_selected_columns(
            SQL_PARSER_TEST.sql_lines, 14)

    def test_find_from_index(self):
        self.assertEqual(14, SQL_PARSER_TEST.instance.find_from_index(
            SQL_PARSER_TEST.sql_lines))

    def test_get_select_columns(self):
        self.assertEqual(['RCTA.CUSTOMER_TRX_ID', 'RCTA.PURCHASE_ORDER', 'RCTLGDA.GL_DATE AS dt_revenue', 'RCTLA.INTERFACE_LINE_ATTRIBUTE1 AS SALES_ORDER', 'GCC.SEGMENT5 AS Wwapc', 'OOHA.ATTRIBUTE1 AS SALES_OFFICE', 'MSIB.SEGMENT1 AS PART_NUMBER'],
                         SQL_PARSER_TEST.instance.get_selected_columns(SQL_PARSER_TEST.sql_lines, 14))

    def test_remove_table_names(self):
        self.assertEqual(['CUSTOMER_TRX_ID', 'PURCHASE_ORDER', 'GL_DATE AS dt_revenue', 'INTERFACE_LINE_ATTRIBUTE1 AS SALES_ORDER', 'SEGMENT5 AS Wwapc',
                          'ATTRIBUTE1 AS SALES_OFFICE', 'SEGMENT1 AS PART_NUMBER'], SQL_PARSER_TEST.instance.remove_table_names(SQL_PARSER_TEST.column_headers))

    def test_format_column_aliases(self):
        self.assertEqual(['RCTA.CUSTOMER_TRX_ID', 'RCTA.PURCHASE_ORDER', 'dt_revenue', 'SALES_ORDER', 'Wwapc',
                          'SALES_OFFICE', 'PART_NUMBER'], SQL_PARSER_TEST.instance.format_column_aliases(SQL_PARSER_TEST.column_headers))

    def test_parse_sql_lines(self):
        self.assertEqual(['CUSTOMER_TRX_ID', 'PURCHASE_ORDER', 'dt_revenue', 'SALES_ORDER',
                          'Wwapc', 'SALES_OFFICE', 'PART_NUMBER'], SQL_PARSER_TEST.instance.parse_sql_file())

    def test_reduce_columns(self):
        self.assertEqual(['DATE', 'PART_PRICE', 'SHIP_AMOUNT', 'ORDER_ID'], SQL_PARSER_TEST.instance.reduce_columns(
            ['SELL_BY_DATE', 'PART_PRICE', 'SHIP_AMOUNT', 'ORDER_ID'], 'DATE'))

    def test_generate_endeca_datatypes(self):
        self.assertEqual(['mdex:dateTime','mdex:double','mdex:double', 'mdex:string'] , SQL_PARSER_TEST.instance.generate_endeca_datatypes(['SELL_BY_DATE', 'PART_PRICE', 'SHIP_AMOUNT', 'ORDER_ID']))