import unittest
from edak import sql_parser as sp


class PARSER(unittest.TestCase):

    @classmethod
    def setUpClass(PARSER):
        PARSER.ins = sp.SQL_PARSER('sql_parser_test_doc.sql')
        PARSER.subq = sp.SQL_PARSER('sql_test_docs/subq_test.sql')

    def test_first_column(self):
        self.assertEqual('CUSTOMER_TRX_ID', PARSER.ins.columns[0])

    def test_second_column(self):
        self.assertEqual('PURCHASE_ORDER', PARSER.ins.columns[1])

    def test_fourth_column(self):
        self.assertEqual('SALES_ORDER', PARSER.ins.columns[3])

    def test_last_column(self):
        self.assertEqual('PART_NUMBER', PARSER.ins.columns[-1])

    def test_parse_sql_file(self):
        self.assertEqual(['CUSTOMER_TRX_ID', 'PURCHASE_ORDER', 'DT_REVENUE', 'SALES_ORDER',
                          'WWAPC', 'SALES_OFFICE', 'PART_NUMBER'], PARSER.ins.columns)

    def test_columns_datatypes(self):
        self.assertEqual([['CUSTOMER_TRX_ID', 'mdex:string'], ['PURCHASE_ORDER', 'mdex:string'], ['DT_REVENUE', 'mdex:dateTime'], ['SALES_ORDER', 'mdex:string'],
                          ['WWAPC','mdex:string'], ['SALES_OFFICE','mdex:string'], ['PART_NUMBER', 'mdex:string']],
                         PARSER.ins.columns_datatypes)

    def test_remove_subq(self):
        self.assertEqual(['PA_TRANS_ID', ' AS PA_GL_PERIOD'], PARSER.subq.remove_subq(['PA_TRANS_ID', '(SELECT DISTINCT PERIOD_NAME FROM APP.PA_PERIODS_ALL) AS PA_GL_PERIOD']))

    def test_subq_first_col(self):
        self.assertEqual('PA_TRANS_ID', PARSER.subq.columns[0])

    def test_subq_sec_col(self):
        self.assertEqual('PA_GL_PERIOD', PARSER.subq.columns[1])

    def test_subq_third_col(self):
        self.assertEqual('DISTRIBUTION_LINE_STATUS', PARSER.subq.columns[2])

    def test_subq_fourth_col(self):
        self.assertEqual('TOTAL_FCST_EQP_COST_PROJ_CURR', PARSER.subq.columns[3])

    def test_split_by_comma_unless_inside_paren(self):
        self.assertEqual(['this','that(the, other thing)'], PARSER.subq.split_by_comma_unless_inside_paren('this,that(the, other thing)'))


    def test_split_by_comma_diagnostic(self):
        self.assertEqual(["as FIELD", " (SELECT FIELD, AS FUCK_ALL)"], PARSER.subq.split_by_comma_unless_inside_paren("as FIELD, (SELECT FIELD, AS FUCK_ALL)"))

    # def test_subq_fifth_col(self):
    #     self.assertEqual('PROJECT_MANAGER', PARSER.subq.columns[4])