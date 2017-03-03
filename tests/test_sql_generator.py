import unittest
from edak import sql_generator
from edak import table_data as td
import sql_generator_test_strings as ts


class SQL(unittest.TestCase):

    @classmethod
    def setUpClass(SQL):
        SQL.sql = sql_generator.SQL(204, 'accounting_period',
                                    'mdex:string', 1, 'Accounting Period', 1, 'FIN')

    def test_attr_b(self):
        self.assertEqual(ts.ATTR_B_COLS + ts.ATTR_B_VALS, SQL.sql.attr_b(SQL.sql.attrs_b,
                                                                         td.ATTRS_B['name'], td.ATTRS_B['columns']))

    def test_attr_b_column_headers(self):
        self.assertEqual(ts.ATTR_B_COLS, SQL.sql.attr_b(SQL.sql.attrs_b,
                                                        td.ATTRS_B['name'], td.ATTRS_B['columns'])[0:562])

    def test_attrs_b_values(self):
        self.assertEqual(ts.ATTR_B_VALS, SQL.sql.attr_b(SQL.sql.attrs_b,
                                                        td.ATTRS_B['name'], td.ATTRS_B['columns'])[562:761])

    def test_attrs_tl_column_headers(self):
        insert_statement = SQL.sql.attr_b(
            ['204', 'accounting_period', 'D', 'Accounting Period'], td.ATTRS_TL['name'], td.ATTRS_TL['columns'])
        self.assertEqual(ts.ATTR_TL_COLS, insert_statement[0:237])

    def test_attrs_tl(self):
        insert_statement = SQL.sql.attr_b(
            SQL.sql.attrs_tl[0], td.ATTRS_TL['name'], td.ATTRS_TL['columns'])
        self.assertEqual(ts.ATTR_TL_VALS, insert_statement[237:421])

    def test_insert_attrs_tl_length(self):
        self.assertEqual(3837, len(SQL.sql.attr_tl(SQL.sql.attrs_tl, td.ATTRS_TL['name'], td.ATTRS_TL['columns'])))

    def test_update_attr_groups(self):
        self.assertEqual("SET EID_INSTANCE_GROUP_ATTR_SEQ = 1, EID_INST_GROUP_ATTR_USER_SEQ = 1 WHERE EID_INSTANCE_ID = 204 AND EID_INSTANCE_ATTRIBUTE = 'accounting_period';",
                         SQL.sql.attr_groups()[27:174])

    def test_create_insert_statement(self):
        column_headers = ['EID_INSTANCE_ID',
                          'EID_INSTANCE_ATTRIBUTE', 'ENDECA_DATATYPE']
        self.assertEqual('Insert into FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE)\n',
                         SQL.sql.insert_statement(td.ATTRS_B['name'], column_headers))

    def test_values(self):
        values = ['204', 'accounting_period', 'mdex:string', '4', 'SYSDATE']
        self.assertEqual("values ( 204,'accounting_period','mdex:string',4,SYSDATE);",
                         SQL.sql.values(*values))

    def test_attr_sql(self):
        self.assertEqual(5136, len(SQL.sql.attr_sql()))

    def test_groups_b_sql(self):
        self.assertEqual(ts.ATTR_GROUPS_B, SQL.sql.groups_b_sql())

    def test_groups_tl_sql(self):
        self.assertEqual(2987, len(SQL.sql.groups_tl_sql()))

    def test_attr_tl_with_args_len(self):
        self.assertEqual(2987, len(SQL.sql.attr_tl(SQL.sql.groups_tl, td.GROUPS_TL['name'], td.GROUPS_TL['columns'])))

    def test_prop_attrs_b(self):
        self.assertEqual(ts.PROP_ATTRS_B, SQL.sql.attrs_b)

    def test_prop_attrs_tl(self):
        self.assertEqual(ts.PROP_ATTRS_TL, SQL.sql.attrs_tl)

    def test_prop_set_attrs_groups(self):
        self.assertEqual(ts.PROP_SET_ATTR_GROUPS, SQL.sql.set_attr_groups)

    def test_prop_groups_b(self):
        self.assertEqual(ts.PROP_GROUPS_B, SQL.sql.groups_b)

    def test_prop_groups_tl(self):
        self.assertEqual(ts.PROP_GROUPS_TL, SQL.sql.groups_tl)

    def test_attr_tl_with_args(self):
        self.assertEqual(SQL.sql.groups_tl_sql(), SQL.sql.attr_tl(SQL.sql.groups_tl, td.GROUPS_TL['name'], td.GROUPS_TL['columns']))


if __name__ == '__main__':
    unittest.main()
