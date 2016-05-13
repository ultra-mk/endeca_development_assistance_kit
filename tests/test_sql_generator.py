import unittest
from edak import sql_generator as s


class SQL_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(SQL_TEST):
		SQL_TEST.sql = s.SQL(204,'accounting_period', 'mdex:string', 1, 'Accounting Period')
		SQL_TEST.instance_id = '204'
		SQL_TEST.define_clause = slice(0,16)
		SQL_TEST.attrs_b_rem_insert = slice(16, 60)
		SQL_TEST.attrs_b_insert = slice(60,627)
		SQL_TEST.attrs_b_values = slice(627,771)
		SQL_TEST.attrs_tl_insert = slice(0,242)
		SQL_TEST.attrs_tl_values = slice(242, 427)
		SQL_TEST.attrs_tl_all_rem_insert = slice(16, 61)
		SQL_TEST.attr_groups_insert = slice(60, 377)
		SQL_TEST.attr_groups_values = slice(378, 469)
		SQL_TEST.update_attr_groups_set = slice(48, 195)
		SQL_TEST.column_name_string = ' (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values'


	def test_init_SQL_attribute(self):
		self.assertEqual('204', SQL_TEST.instance_id)
	

	def test_insert_attrs_b_define_clause(self):
		self.assertEqual('SET DEFINE OFF;\n', SQL_TEST.sql.insert_attrs_b[SQL_TEST.define_clause])
	

	def test_insert_attrs_b_rem_clause(self):
		self.assertEqual('REM INSERTING into APPS.FND_EID_PDR_ATTRS_B\n', SQL_TEST.sql.insert_attrs_b[SQL_TEST.attrs_b_rem_insert])
		

	def test_insert_attrs_b_column_headers(self):
		self.assertEqual('Insert into APPS.FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE,EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG,DIM_ENABLE_REFINEMENTS_FLAG,DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG,MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,ATTR_VALUE_SET_FLAG,VALUE_SET_NAME,ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME)\n', SQL_TEST.sql.insert_attrs_b[SQL_TEST.attrs_b_insert])


	def test_insert_attrs_b_values(self):
		self.assertEqual("values ( 204,'accounting_period','mdex:string',1,'2.3','MSI','N','N','N','N','N','N','N',0,0,SYSDATE,0,SYSDATE,0,null,null,null,null,null,null);", SQL_TEST.sql.insert_attrs_b[SQL_TEST.attrs_b_values])


	def test_insert_attrs_tl_column_headers(self):
		insert_statement = SQL_TEST.sql.insert_attrs_tl(SQL_TEST.instance_id, 'accounting_period', 'D','Accounting Period', 'FND_EID_PDR_ATTRS_TL')
		self.assertEqual('Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN)\n', insert_statement[SQL_TEST.attrs_tl_insert])


	def test_insert_attrs_tl_values(self):
		insert_statement = SQL_TEST.sql.insert_attrs_tl(SQL_TEST.instance_id, 'accounting_period', 'D','Accounting Period', 'FND_EID_PDR_ATTRS_TL')
		self.assertEqual("values ( 204,'accounting_period','D','US','Accounting Period','Accounting Period','Accounting Period','Accounting Period',0,SYSDATE,0,SYSDATE,0);", insert_statement[SQL_TEST.attrs_tl_values])


	def test_insert_attrs_tl_all_define_clause(self):
		insert_statement = SQL_TEST.sql.insert_attrs_tl_all
		self.assertEqual('SET DEFINE OFF;\n', insert_statement[SQL_TEST.define_clause])


	def test_insert_attrs_tl_all_rem_clause(self):
		insert_statement = SQL_TEST.sql.insert_attrs_tl_all
		self.assertEqual('REM INSERTING into APPS.FND_EID_PDR_ATTRS_TL\n', insert_statement[SQL_TEST.attrs_tl_all_rem_insert])


	def test_insert_attrs_tl_length(self):
		insert_statement = SQL_TEST.sql.insert_attrs_tl_all
		self.assertEqual(3957, len(SQL_TEST.sql.insert_attrs_tl_all))


	def test_insert_attrs_tl_all_commit(self):
		insert_statement = SQL_TEST.sql.insert_attrs_tl_all
		self.assertEqual('COMMIT;', SQL_TEST.sql.insert_attrs_tl_all[-7:])


	def test_insert_attrs_groups_set_define_clause(self):
		self.assertEqual('SET DEFINE OFF;\n', SQL_TEST.sql.insert_attr_groups[SQL_TEST.define_clause])

		
	def test_insert_attrs_group_column_headers(self):
		self.assertEqual('Insert into APPS.FND_EID_ATTR_GROUPS (EID_INSTANCE_ID,EID_INSTANCE_GROUP,EID_INSTANCE_ATTRIBUTE,EID_INSTANCE_GROUP_ATTR_SEQ,EID_INST_GROUP_ATTR_USER_SEQ,GROUP_ATTRIBUTE_SOURCE,EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN)', SQL_TEST.sql.insert_attr_groups[SQL_TEST.attr_groups_insert])

	
	def test_insert_attrs_group_values(self):
		self.assertEqual("values ( 204,'Categories','accounting_period',1,1,'MSI','2.3','N',0,0,SYSDATE,0,SYSDATE,0);", SQL_TEST.sql.insert_attr_groups[SQL_TEST.attr_groups_values])


	def test_update_attr_groups(self):
		self.assertEqual("SET EID_INSTANCE_GROUP_ATTR_SEQ = 1, EID_INST_GROUP_ATTR_USER_SEQ = 1 WHERE EID_INSTANCE_ID = 204 AND EID_INSTANCE_ATTRIBUTE = 'accounting_period';", SQL_TEST.sql.update_attr_groups[SQL_TEST.update_attr_groups_set])


	def test_concat_schema_table(self):
		self.assertEqual('APPS.FND_EID_ATTRS_B', SQL_TEST.sql.concat_schema_table('APPS', 'FND_EID_ATTRS_B'))


	def test_create_column_name_string(self):
		column_headers = ['EID_INSTANCE_ID','EID_INSTANCE_GROUP','EID_INSTANCE_ATTRIBUTE','EID_INSTANCE_GROUP_ATTR_SEQ']
		self.assertEqual(' (EID_INSTANCE_ID,EID_INSTANCE_GROUP,EID_INSTANCE_ATTRIBUTE,EID_INSTANCE_GROUP_ATTR_SEQ)\n', SQL_TEST.sql.create_column_name_string(*column_headers))


	def test_create_values_string(self):
		values = ['204', 'accounting_period', 'mdex:string', '4']
		self.assertEqual("values ( 204,'accounting_period','mdex:string',4);", SQL_TEST.sql.create_values_string(*values))


if __name__ == '__main__':
	unittest.main()