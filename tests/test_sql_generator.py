import unittest
from edak import sql_generator


class SQL(unittest.TestCase):

    @classmethod
    def setUpClass(SQL):
        SQL.sql = sql_generator.SQL(204, 'accounting_period',
                                    'mdex:string', 1, 'Accounting Period')
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

    def test_insert_attrs_b_define_clause(self):
        self.assertEqual('SET DEFINE OFF;\n', SQL.sql.insert_attrs_b[0:16])

    def test_insert_attrs_b_rem_clause(self):
        self.assertEqual('REM INSERTING into FND_EID_PDR_ATTRS_B\n',
                         SQL.sql.insert_attrs_b[16:55])

    def test_insert_attrs_b_column_headers(self):
        self.assertEqual(SQL.attr_b_cols, SQL.sql.insert_attrs_b[55:617])

    def test_insert_attrs_b_values(self):
        self.assertEqual(SQL.attr_b_vals, SQL.sql.insert_attrs_b[617:761])

    def test_insert_attrs_tl_column_headers(self):
        insert_statement = SQL.sql.insert_attrs_tl(
            SQL.instance_id, 'accounting_period', 'D', 'Accounting Period', 'FND_EID_PDR_ATTRS_TL')
        self.assertEqual(SQL.attr_tl_cols,insert_statement[0:237])

    def test_insert_attrs_tl_values(self):
        insert_statement = SQL.sql.insert_attrs_tl(
            SQL.instance_id, 'accounting_period', 'D', 'Accounting Period', 'FND_EID_PDR_ATTRS_TL')
        self.assertEqual(SQL.attr_tl_vals, insert_statement[237:421])

    def test_insert_attrs_tl_all_define_clause(self):
        self.assertEqual('SET DEFINE OFF;\n',
                         SQL.sql.insert_attrs_tl_all[0:16])

    def test_insert_attrs_tl_all_rem_clause(self):
        insert_statement = SQL.sql.insert_attrs_tl_all
        self.assertEqual('REM INSERTING into FND_EID_PDR_ATTRS_TL\n',
                         insert_statement[16:56])

    def test_insert_attrs_tl_length(self):
        self.assertEqual(3902, len(SQL.sql.insert_attrs_tl_all))

    def test_insert_attrs_tl_all_commit(self):
        insert_statement = SQL.sql.insert_attrs_tl_all
        self.assertEqual('COMMIT;', SQL.sql.insert_attrs_tl_all[-7:])

    def test_insert_attrs_groups_set_define_clause(self):
        self.assertEqual('SET DEFINE OFF;\n', SQL.sql.insert_attr_groups[0:16])

    def test_insert_attrs_group_column_headers(self):
        self.assertEqual(SQL.attr_groups_cols, SQL.sql.insert_attr_groups[55:367])

    def test_insert_attrs_group_values(self):
        self.assertEqual("values ( 204,'Categories','accounting_period',1,1,'MSI','2.3','N',0,0,SYSDATE,0,SYSDATE,0);",
                         SQL.sql.insert_attr_groups[368:459])

    def test_update_attr_groups(self):
        self.assertEqual("SET EID_INSTANCE_GROUP_ATTR_SEQ = 1, EID_INST_GROUP_ATTR_USER_SEQ = 1 WHERE EID_INSTANCE_ID = 204 AND EID_INSTANCE_ATTRIBUTE = 'accounting_period';",
                         SQL.sql.update_attr_groups[43:190])

    def test_create_insert_statement(self):
        column_headers = ['EID_INSTANCE_ID',
                          'EID_INSTANCE_ATTRIBUTE', 'ENDECA_DATATYPE']
        self.assertEqual('Insert into FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE)\n',
                         SQL.sql.create_insert_statement(SQL.sql.ATTRS_B, column_headers))

    # def test_concat_schema_table(self):
    #     self.assertEqual('APPS.FND_EID_ATTRS_B', SQL.sql.concat_schema_table(
    #         'APPS', 'FND_EID_ATTRS_B'))

    def test_create_column_name_string(self):
        column_headers = ['EID_INSTANCE_ID', 'EID_INSTANCE_GROUP',
                          'EID_INSTANCE_ATTRIBUTE', 'EID_INSTANCE_GROUP_ATTR_SEQ']
        self.assertEqual(' (EID_INSTANCE_ID,EID_INSTANCE_GROUP,EID_INSTANCE_ATTRIBUTE,EID_INSTANCE_GROUP_ATTR_SEQ)\n',
                         SQL.sql.create_column_name_string(*column_headers))

    def test_create_values_string(self):
        values = ['204', 'accounting_period', 'mdex:string', '4']
        self.assertEqual("values ( 204,'accounting_period','mdex:string',4);",
                         SQL.sql.create_values_string(*values))


if __name__ == '__main__':
    unittest.main()
