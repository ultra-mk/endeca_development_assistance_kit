import unittest
from edak import sql_generator
import table_data as td


class SQL(unittest.TestCase):

    @classmethod
    def setUpClass(SQL):
        SQL.sql = sql_generator.SQL(204, 'accounting_period',
                                    'mdex:string', 1, 'Accounting Period', 1, 'FIN')

        SQL.instance_id = '204'
        SQL.column_name_string = ("  (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,"
                                  "ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,"
                                  "LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values")

        SQL.attr_b_cols = ("Insert into FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,"
                           "ENDECA_DATATYPE,EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,"
                           "MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG,DIM_ENABLE_REFINEMENTS_FLAG,"
                           "DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG,"
                           "MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,"
                           "CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,"
                           "ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,ATTR_VALUE_SET_FLAG,VALUE_SET_NAME,"
                           "ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME)\n")

        SQL.attr_b_vals = ("values ( 204,'accounting_period','mdex:string',1,'2.3',"
                           "'MSI','N','N','N','N','N','N','N',0,0,SYSDATE,0,SYSDATE,0,"
                           "null,null,null,null,null,null);")

        SQL.attr_tl_cols = ("Insert into FND_EID_PDR_ATTRS_TL "
                            "(EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,"
                            "DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,"
                            "CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN)\n")

        SQL.attr_tl_vals = ("values ( 204,'accounting_period','D','US','Accounting Period',"
                            "'Accounting Period','Accounting Period','Accounting Period',0,"
                            "SYSDATE,0,SYSDATE,0);")

        SQL.attr_groups_cols = ("Insert into FND_EID_ATTR_GROUPS "
                                "(EID_INSTANCE_ID,EID_INSTANCE_GROUP,EID_INSTANCE_ATTRIBUTE,"
                                "EID_INSTANCE_GROUP_ATTR_SEQ,EID_INST_GROUP_ATTR_USER_SEQ,"
                                "GROUP_ATTRIBUTE_SOURCE,EID_RELEASE_VERSION,OBSOLETED_FLAG,"
                                "OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE,"
                                "LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN)")

        SQL.groups_b = ("Insert into FND_EID_GROUPS_B (EID_INSTANCE_ID,EID_INSTANCE_GROUP,"
                        "EID_RELEASE_VERSION,EID_INSTANCE_GROUP_SEQ,EID_INSTANCE_GROUP_USER_SEQ,"
                        "GROUP_SOURCE,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,"
                        "CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN)"
                        "\nvalues ( 204,'FIN','2.3',1,1,'MSI','N',0,0,SYSDATE,0,SYSDATE,0);")

    def test_insert_single_attr_b(self):
        self.assertEqual(SQL.attr_b_cols + SQL.attr_b_vals, SQL.sql.insert_single_attr(SQL.sql.attrs_b_values,
                                                                                       td.ATTRS_B['name'], td.ATTRS_B['columns']))

    def test_create_attrs_tl_values_len(self):
        self.assertEqual(10, len(SQL.sql.attrs_tl_values))

    def test_create_attrs_tl_values(self):
        self.assertEqual(['204', 'accounting_period', 'D', 'US',
                          'Accounting Period', 'Accounting Period', 'Accounting Period',
                          'Accounting Period', '0', 'SYSDATE', '0', 'SYSDATE', '0'], SQL.sql.attrs_tl_values[0])

    def test_insert_attrs_b_column_headers(self):
        self.assertEqual(SQL.attr_b_cols, SQL.sql.insert_single_attr(SQL.sql.attrs_b_values,
                                                                     td.ATTRS_B['name'], td.ATTRS_B['columns'])[0:562])

    def test_insert_attrs_b_values(self):
        self.assertEqual(SQL.attr_b_vals, SQL.sql.insert_single_attr(SQL.sql.attrs_b_values,
                                                                     td.ATTRS_B['name'], td.ATTRS_B['columns'])[562:761])

    def test_insert_attrs_tl_column_headers(self):
        insert_statement = SQL.sql.insert_single_attr(
            [SQL.instance_id, 'accounting_period', 'D', 'Accounting Period'], td.ATTRS_TL['name'], td.ATTRS_TL['columns'])
        self.assertEqual(SQL.attr_tl_cols, insert_statement[0:237])

    def test_insert_attrs_tl_values(self):
        insert_statement = SQL.sql.insert_single_attr(
            SQL.sql.attrs_tl_values[0], td.ATTRS_TL['name'], td.ATTRS_TL['columns'])
        self.assertEqual(SQL.attr_tl_vals, insert_statement[237:421])

    def test_insert_attrs_tl_length(self):
        self.assertEqual(3838, len(SQL.sql.insert_attrs_tl_all()))

    def test_update_attr_groups(self):
        self.assertEqual("SET EID_INSTANCE_GROUP_ATTR_SEQ = 1, EID_INST_GROUP_ATTR_USER_SEQ = 1 WHERE EID_INSTANCE_ID = 204 AND EID_INSTANCE_ATTRIBUTE = 'accounting_period';",
                         SQL.sql.update_attr_groups()[27:174])

    def test_create_insert_statement(self):
        column_headers = ['EID_INSTANCE_ID',
                          'EID_INSTANCE_ATTRIBUTE', 'ENDECA_DATATYPE']
        self.assertEqual('Insert into FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE)\n',
                         SQL.sql.create_insert_statement(td.ATTRS_B['name'], column_headers))

    def test_create_values_string(self):
        values = ['204', 'accounting_period', 'mdex:string', '4']
        self.assertEqual("values ( 204,'accounting_period','mdex:string',4);",
                         SQL.sql.create_values_string(*values))

    def test_attr_sql(self):
        self.assertEqual(5137, len(SQL.sql.attr_sql()))

    def test_generate_groups_b_sql(self):
        self.assertEqual(SQL.groups_b, SQL.sql.generate_groups_b_sql())

    def test_generate_groups_tl_sql(self):
        self.assertEqual(2988, len(SQL.sql.generate_groups_tl_sql()))

if __name__ == '__main__':
    unittest.main()
