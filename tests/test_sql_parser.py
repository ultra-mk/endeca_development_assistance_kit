import unittest
from edak import sql_parser as sp


class PARSER(unittest.TestCase):
    diag_text = ("PEIA.EXPENDITURE_ITEM_ID AS PA_TRANS_ID,"
                 "(SELECT DISTINCT PERIOD_NAME FROM APPS.PA_PERIODS_ALL WHERE PCDLA.GL_DATE BETWEEN START_DATE AND END_DATE) AS PA_GL_PERIOD,"
                 "CASE PCDLA.TRANSFER_STATUS_CODE"
                 "WHEN 'A' THEN 'Accepted'"
                 "WHEN 'R' THEN 'Rejected'"
                 "WHEN 'P' THEN 'Pending'"
                 "WHEN 'T' THEN 'Transferred'"
                 "WHEN 'X' THEN 'Rejected In Transfer'"
                 "WHEN 'V' THEN 'Received'"
                 "ELSE 'N/A'"
                "END AS DISTRIBUTION_LINE_STATUS,"
"(MFB.UNIT_SELLING_PRICE * MFB.QUANTITY * 1.005) AS TOTAL_FCST_EQP_COST_PROJ_CURR,")
# (SELECT DISTINCT PAPF.FULL_NAME FROM APPS.PER_ALL_PEOPLE_F PAPF, APPS.PA_PROJECT_PLAYERS PPP WHERE PAPF.PERSON_ID = PPP.PERSON_ID AND PPP.PROJECT_ROLE_TYPE = 'PROJECT MANAGER' AND PPP.END_DATE_ACTIVE IS NULL AND PPA.PROJECT_ID = PPP.PROJECT_ID) AS PROJECT_MANAGER"

    diag_list = ["PEIA.EXPENDITURE_ITEM_ID AS PA_TRANS_ID",
                "(SELECT DISTINCT PERIOD_NAME FROM APPS.PA_PERIODS_ALL WHERE PCDLA.GL_DATE BETWEEN START_DATE AND END_DATE) AS PA_GL_PERIOD",
                 ( "CASE PCDLA.TRANSFER_STATUS_CODE"
                 "WHEN 'A' THEN 'Accepted'"
                 "WHEN 'R' THEN 'Rejected'"
                 "WHEN 'P' THEN 'Pending'"
                 "WHEN 'T' THEN 'Transferred'"
                 "WHEN 'X' THEN 'Rejected In Transfer'"
                 "WHEN 'V' THEN 'Received'"
                 "ELSE 'N/A'"
                "END AS DISTRIBUTION_LINE_STATUS"),
                 "(MFB.UNIT_SELLING_PRICE * MFB.QUANTITY * 1.005) AS TOTAL_FCST_EQP_COST_PROJ_CURR",
                 '']

    @classmethod
    def setUpClass(PARSER):
        PARSER.ins = sp.SQL_PARSER('sql_test_docs/sql_parser_test_doc.sql')
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


    def test_diag_text(self):
        self.assertEqual(PARSER.diag_list, PARSER.subq.split_by_comma_unless_inside_paren(PARSER.diag_text))

    
    # def test_subq_fifth_col(self):
    #     self.assertEqual('PROJECT_MANAGER', PARSER.subq.columns[4])