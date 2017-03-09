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
        self.assertEqual(ts.ATTRS_B, SQL.sql.attr_b(td.ATTRS_B, SQL.sql.attrs_b))

    def test_attr_tl(self):
        self.assertEqual(ts.ATTRS_TL, SQL.sql.attr_tl(td.ATTRS_TL, SQL.sql.attrs_tl))
    
    def test_attr_groups(self):
        self.assertEqual(ts.ATTR_GROUPS, SQL.sql.attr_b(td.ATTR_GROUPS, SQL.sql.attrs_group))

    def test_update_sequence(self):
        self.assertEqual(ts.UPDATE_SEQUENCE, SQL.sql.update_sequence())

    def test_groups_b(self):
        self.assertEqual(ts.GROUPS_B, SQL.sql.attr_b(td.GROUPS_B, SQL.sql.groups_b))

    def test_groups_tl(self):
        self.assertEqual(ts.GROUPS_TL, SQL.sql.attr_tl(td.GROUPS_TL, SQL.sql.groups_tl))

    def test_build_sql_attrs(self):
        self.assertEqual('\n'.join(['SET DEFINE OFF;', ts.ATTRS_B, ts.ATTRS_TL, ts.ATTR_GROUPS, ts.UPDATE_SEQUENCE]), SQL.sql.build_sql(['SET DEFINE OFF;', SQL.sql.attr_b(td.ATTRS_B, SQL.sql.attrs_b), 
                SQL.sql.attr_tl(td.ATTRS_TL, SQL.sql.attrs_tl), SQL.sql.attr_b(td.ATTR_GROUPS, SQL.sql.attrs_group),
                SQL.sql.update_sequence()]))

    def test_group_sql(self):
        self.assertEqual('\n'.join([ts.GROUPS_B, ts.GROUPS_TL]), SQL.sql.build_sql([SQL.sql.attr_b(td.GROUPS_B, SQL.sql.groups_b), SQL.sql.attr_tl(td.GROUPS_TL, SQL.sql.groups_tl)]))

if __name__ == '__main__':
    unittest.main()
