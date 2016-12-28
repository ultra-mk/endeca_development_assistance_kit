import unittest
from edak import sql_parser as sp
from edak import utils


class PARSER(unittest.TestCase):

    @classmethod
    def setUpClass(PARSER):
        PARSER.instance = sp.SQL_PARSER('sql_parser_test_doc.sql')
        PARSER.sql_lines = utils.open_file_split_into_lines(
            'sql_parser_test_doc.sql')
        PARSER.column_headers = PARSER.instance.get_selected_columns(
            PARSER.sql_lines, 14)
        PARSER.new = sp.SQL_PARSER_NEW('sql_parser_test_doc.sql')

    def test_find_index(self):
        self.assertEqual(14, PARSER.instance.find_index(
            PARSER.sql_lines, 'FROM '))

    def test_get_select_columns(self):
        self.assertEqual(['RCTA.CUSTOMER_TRX_ID', 'RCTA.PURCHASE_ORDER', 'RCTLGDA.GL_DATE AS dt_revenue', 'RCTLA.INTERFACE_LINE_ATTRIBUTE1 AS SALES_ORDER', 'GCC.SEGMENT5 AS Wwapc', 'OOHA.ATTRIBUTE1 AS SALES_OFFICE', 'MSIB.SEGMENT1 AS PART_NUMBER'],
                         PARSER.instance.get_selected_columns(PARSER.sql_lines, 14))

    def test_remove_table_names(self):
        self.assertEqual(['CUSTOMER_TRX_ID', 'PURCHASE_ORDER', 'GL_DATE AS dt_revenue', 'INTERFACE_LINE_ATTRIBUTE1 AS SALES_ORDER', 'SEGMENT5 AS Wwapc',
                          'ATTRIBUTE1 AS SALES_OFFICE', 'SEGMENT1 AS PART_NUMBER'], PARSER.instance.remove_table_names(PARSER.column_headers))

    def test_format_column_aliases(self):
        self.assertEqual(['RCTA.CUSTOMER_TRX_ID', 'RCTA.PURCHASE_ORDER', 'dt_revenue', 'SALES_ORDER', 'Wwapc',
                          'SALES_OFFICE', 'PART_NUMBER'], PARSER.instance.format_column_aliases(PARSER.column_headers))

    def test_parse_sql_lines(self):
        self.assertEqual(['CUSTOMER_TRX_ID', 'PURCHASE_ORDER', 'dt_revenue', 'SALES_ORDER',
                          'Wwapc', 'SALES_OFFICE', 'PART_NUMBER'], PARSER.instance.parse_sql_file())

    def test_generate_endeca_datatypes(self):
        self.assertEqual([['FULFILLMENT_DATE', 'mdex:dateTime'], ['UNIT_PRICE', 'mdex:double'], ['SHIP_QUANTITY', 'mdex:int'], ['ORDER_ID', 'mdex:string']],
                         PARSER.instance.generate_endeca_datatypes(['FULFILLMENT_DATE', 'UNIT_PRICE', 'SHIP_QUANTITY', 'ORDER_ID']))

##additional tests for alternate implementation
    def test_first_column_SQL_PARSER_NEW(self):
        self.assertEqual('CUSTOMER_TRX_ID', PARSER.new.columns[0])

    def test_second_column_SQL_PARSER_NEW(self):
        self.assertEqual('PURCHASE_ORDER', PARSER.new.columns[1])

    def test_fourth_column_SQL_PARSER_NEW(self):
        self.assertEqual('SALES_ORDER', PARSER.new.columns[3])

    def test_last_column_SQL_PARSER_NEW(self):
        self.assertEqual('PART_NUMBER', PARSER.new.columns[-1])

    def test_parse_sql_file_SQL_PARTSER_NEW(self):
        self.assertEqual(['CUSTOMER_TRX_ID', 'PURCHASE_ORDER', 'DT_REVENUE', 'SALES_ORDER',
                          'WWAPC', 'SALES_OFFICE', 'PART_NUMBER'], PARSER.new.columns)

    def test_generate_endeca_datatypes(self):
        self.assertEqual([['CUSTOMER_TRX_ID', 'mdex:string'], ['PURCHASE_ORDER', 'mdex:string'], ['DT_REVENUE', 'mdex:dateTime'], ['SALES_ORDER', 'mdex:string'],
                          ['WWAPC','mdex:string'], ['SALES_OFFICE','mdex:string'], ['PART_NUMBER', 'mdex:string']],
                         PARSER.new.endeca_datatypes)

