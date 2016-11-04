import unittest
from edak import sql_generator
import table_data as td
import sql_generator_test_strings as test_strings


class SQL(unittest.TestCase):

    @classmethod
    def setUpClass(SQL):
        SQL.sql = sql_generator.SQL(204, 'accounting_period',
                                    'mdex:string', 1, 'Accounting Period', 1, 'FIN')

        SQL.instance_id = '204'

    def test_attr_b(self):
        self.assertEqual(test_strings.ATTR_B_COLS + test_strings.ATTR_B_VALS, SQL.sql.attr_b(SQL.sql.attrs_b,
                                                                                       td.ATTRS_B['name'], td.ATTRS_B['columns']))

    def test_attr_tl_values_len(self):
        self.assertEqual(10, len(SQL.sql.attrs_tl))

    def test_attr_tl_values(self):
        self.assertEqual(['204', 'accounting_period', 'D', 'US',
                          'Accounting Period', 'Accounting Period', 'Accounting Period',
                          'Accounting Period', '0', 'SYSDATE', '0', 'SYSDATE', '0'], SQL.sql.attrs_tl[0])

    def test_attr_b_column_headers(self):
        self.assertEqual(test_strings.ATTR_B_COLS, SQL.sql.attr_b(SQL.sql.attrs_b,
                                                                     td.ATTRS_B['name'], td.ATTRS_B['columns'])[0:562])

    def test_attrs_b_values(self):
        self.assertEqual(test_strings.ATTR_B_VALS, SQL.sql.attr_b(SQL.sql.attrs_b,
                                                                     td.ATTRS_B['name'], td.ATTRS_B['columns'])[562:761])

    def test_attrs_tl_column_headers(self):
        insert_statement = SQL.sql.attr_b(
            [SQL.instance_id, 'accounting_period', 'D', 'Accounting Period'], td.ATTRS_TL['name'], td.ATTRS_TL['columns'])
        self.assertEqual(test_strings.ATTR_TL_COLS, insert_statement[0:237])

    def test_attrs_tl(self):
        insert_statement = SQL.sql.attr_b(
            SQL.sql.attrs_tl[0], td.ATTRS_TL['name'], td.ATTRS_TL['columns'])
        self.assertEqual(test_strings.ATTR_TL_VALS, insert_statement[237:421])

    def test_insert_attrs_tl_length(self):
        self.assertEqual(3837, len(SQL.sql.attr_tl()))

    def test_update_attr_groups(self):
        self.assertEqual("SET EID_INSTANCE_GROUP_ATTR_SEQ = 1, EID_INST_GROUP_ATTR_USER_SEQ = 1 WHERE EID_INSTANCE_ID = 204 AND EID_INSTANCE_ATTRIBUTE = 'accounting_period';",
                         SQL.sql.attr_groups()[27:174])

    def test_create_insert_statement(self):
        column_headers = ['EID_INSTANCE_ID',
                          'EID_INSTANCE_ATTRIBUTE', 'ENDECA_DATATYPE']
        self.assertEqual('Insert into FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE)\n',
                         SQL.sql.insert_statement(td.ATTRS_B['name'], column_headers))

    def test_values(self):
        values = ['204', 'accounting_period', 'mdex:string', '4','SYSDATE']
        self.assertEqual("values ( 204,'accounting_period','mdex:string',4,SYSDATE);",
                         SQL.sql.values(*values))

    def test_attr_sql(self):
        self.assertEqual(5136, len(SQL.sql.attr_sql()))

    def test_groups_b_sql(self):
        self.assertEqual(test_strings.ATTR_GROUPS_B, SQL.sql.groups_b_sql())

    def test_groups_tl_sql(self):
        self.assertEqual(2987, len(SQL.sql.groups_tl_sql()))

if __name__ == '__main__':
    unittest.main()
