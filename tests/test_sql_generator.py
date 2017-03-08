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
        self.assertEqual(ts.ATTRS_B, SQL.sql.attr_b(td.ATTRS_B['name'], td.ATTRS_B['columns'], SQL.sql.attrs_b))

    def test_attr_tl(self):
        self.assertEqual(ts.ATTRS_TL, SQL.sql.attr_tl(td.ATTRS_TL['name'], td.ATTRS_TL['columns'], SQL.sql.attrs_tl))
    
    def test_attr_groups(self):
        self.assertEqual(ts.ATTR_GROUPS, SQL.sql.attr_b(td.ATTR_GROUPS['name'], td.ATTR_GROUPS['columns'], SQL.sql.attrs_group))

    # def test_attr_sql(self):
    #     self.assertEqual(5136, len(SQL.sql.attr_sql()))

    # def test_update_attr_groups(self):
    #     self.assertEqual("SET EID_INSTANCE_GROUP_ATTR_SEQ = 1, EID_INST_GROUP_ATTR_USER_SEQ = 1 WHERE EID_INSTANCE_ID = 204 AND EID_INSTANCE_ATTRIBUTE = 'accounting_period';",
    #                      SQL.sql.attr_groups()[27:174])



    # def test_groups_b_sql(self):
    #     self.assertEqual(ts.ATTR_GROUPS_B, SQL.sql.groups_b_sql())

    # def test_groups_tl_sql(self):
    #     self.assertEqual(2987, len(SQL.sql.groups_tl_sql()))

    # def test_attr_tl_with_args_len(self):
    #     self.assertEqual(2987, len(SQL.sql.attr_tl(SQL.sql.groups_tl, td.GROUPS_TL['name'], td.GROUPS_TL['columns'])))

    # def test_prop_attrs_b(self):
    #     self.assertEqual(ts.PROP_ATTRS_B, SQL.sql.attrs_b)

    # def test_prop_attrs_tl(self):
    #     self.assertEqual(ts.PROP_ATTRS_TL, SQL.sql.attrs_tl)

    # def test_prop_set_attrs_groups(self):
    #     self.assertEqual(ts.PROP_SET_ATTR_GROUPS, SQL.sql.set_attr_groups)

    # def test_prop_groups_b(self):
    #     self.assertEqual(ts.PROP_GROUPS_B, SQL.sql.groups_b)

    # def test_prop_groups_tl(self):
    #     self.assertEqual(ts.PROP_GROUPS_TL, SQL.sql.groups_tl)

    # def test_attr_tl_with_args(self):
    #     self.assertEqual(SQL.sql.groups_tl_sql(), SQL.sql.attr_tl(SQL.sql.groups_tl, td.GROUPS_TL['name'], td.GROUPS_TL['columns']))


if __name__ == '__main__':
    unittest.main()
