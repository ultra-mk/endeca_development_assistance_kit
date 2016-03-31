import unittest
import eee_sql as e

class EEE_SQL_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(EEE_SQL_TEST):
		EEE_SQL_TEST.sql = e.SQL(204,'accounting_period', 'mdex:string', 1, 'Accounting Period')
		EEE_SQL_TEST.define_clause = slice(0,16)
		EEE_SQL_TEST.attrs_b_rem_insert = slice(16, 60)
		EEE_SQL_TEST.attrs_b_insert = slice(60,632)
		EEE_SQL_TEST.attrs_b_values = slice(632,770)
		EEE_SQL_TEST.attrs_tl_rem_insert = slice(16, 61)
		EEE_SQL_TEST.attrs_tl_insert = slice(61,309)
		EEE_SQL_TEST.attrs_tl_values = slice(309, 436)


	def test_init_SQL_attribute(self):
		self.assertEqual('204', EEE_SQL_TEST.sql.eid_instance_id)
		self.assertEqual('accounting_period', EEE_SQL_TEST.sql.eid_instance_attribute) 
		self.assertEqual('mdex:string', EEE_SQL_TEST.sql.datatype)
		self.assertEqual('1', EEE_SQL_TEST.sql.profile_id)
		self.assertEqual('Accounting Period', EEE_SQL_TEST.sql.display_name)
		

	def test_insert_attrs_b(self):
		self.assertEqual('SET DEFINE OFF;\n', EEE_SQL_TEST.sql.insert_attrs_b[EEE_SQL_TEST.define_clause])
		self.assertEqual('REM INSERTING into APPS.FND_EID_PDR_ATTRS_B\n', EEE_SQL_TEST.sql.insert_attrs_b[EEE_SQL_TEST.attrs_b_rem_insert])
		self.assertEqual('Insert into APPS.FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE, EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG, DIM_ENABLE_REFINEMENTS_FLAG,DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG, MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE, LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,ATTR_VALUE_SET_FLAG, VALUE_SET_NAME,ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME)\n', EEE_SQL_TEST.sql.insert_attrs_b[EEE_SQL_TEST.attrs_b_insert])
		self.assertEqual("(204,'accounting_period','mdex:string',1,'2.3','MSI','N','N','N','N','N','N','N','0',0,SYSDATE,0,SYSDATE,0,null,null,null,null,null,null);", EEE_SQL_TEST.sql.insert_attrs_b[EEE_SQL_TEST.attrs_b_values])

	def test_insert_attrs_tl(self):
		self.assertEqual('SET DEFINE OFF;\n', EEE_SQL_TEST.sql.insert_attrs_tl[EEE_SQL_TEST.define_clause])
		self.assertEqual('REM INSERTING into APPS.FND_EID_PDR_ATTRS_TL\n', EEE_SQL_TEST.sql.insert_attrs_tl[EEE_SQL_TEST.attrs_tl_rem_insert])
		self.assertEqual('Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values', EEE_SQL_TEST.sql.insert_attrs_tl[EEE_SQL_TEST.attrs_tl_insert])
		self.assertEqual("(204,'accounting_date','D','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);", EEE_SQL_TEST.sql.insert_attrs_tl[EEE_SQL_TEST.attrs_tl_values])




if __name__ == '__main__':
	unittest.main()