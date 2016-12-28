import unittest
from edak import sql_parser as sp


class PARSER(unittest.TestCase):

    @classmethod
    def setUpClass(PARSER):
        PARSER.ins = sp.SQL_PARSER('sql_parser_test_doc.sql')

    def test_first_column_SQL_PARSER_NEW(self):
        self.assertEqual('CUSTOMER_TRX_ID', PARSER.ins.columns[0])

    def test_second_column_SQL_PARSER_NEW(self):
        self.assertEqual('PURCHASE_ORDER', PARSER.ins.columns[1])

    def test_fourth_column_SQL_PARSER_NEW(self):
        self.assertEqual('SALES_ORDER', PARSER.ins.columns[3])

    def test_last_column_SQL_PARSER_NEW(self):
        self.assertEqual('PART_NUMBER', PARSER.ins.columns[-1])

    def test_parse_sql_file_SQL_PARTSER_NEW(self):
        self.assertEqual(['CUSTOMER_TRX_ID', 'PURCHASE_ORDER', 'DT_REVENUE', 'SALES_ORDER',
                          'WWAPC', 'SALES_OFFICE', 'PART_NUMBER'], PARSER.ins.columns)

    def test_generate_endeca_datatypes(self):
        self.assertEqual([['CUSTOMER_TRX_ID', 'mdex:string'], ['PURCHASE_ORDER', 'mdex:string'], ['DT_REVENUE', 'mdex:dateTime'], ['SALES_ORDER', 'mdex:string'],
                          ['WWAPC','mdex:string'], ['SALES_OFFICE','mdex:string'], ['PART_NUMBER', 'mdex:string']],
                         PARSER.ins.columns_datatypes)

