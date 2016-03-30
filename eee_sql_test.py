import unittest
import eee_sql as e

class EEE_SQL_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(EEE_SQL_TEST):
		EEE_SQL_TEST.insert_attr = e.Insert_attribute(204,'accounting_period', 'mdex:string')
		EEE_SQL_TEST.define_clause = slice(0,16)
		EEE_SQL_TEST.rem_insert = slice(16, 60)
		EEE_SQL_TEST.insert = slice(60,632)
		EEE_SQL_TEST.values = slice(632,768)


	def test_init_Insert_attribute(self):
		self.assertEqual(204, EEE_SQL_TEST.insert_attr.eid_instance_id)
		self.assertEqual('accounting_period', EEE_SQL_TEST.insert_attr.eid_instance_attribute) 
		self.assertEqual('mdex:string', EEE_SQL_TEST.insert_attr.datatype)
		self.assertEqual('SET DEFINE OFF;\n', EEE_SQL_TEST.insert_attr.sql[EEE_SQL_TEST.define_clause])
		self.assertEqual('REM INSERTING into APPS.FND_EID_PDR_ATTRS_B\n', EEE_SQL_TEST.insert_attr.sql[EEE_SQL_TEST.rem_insert])
		self.assertEqual('Insert into APPS.FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE, EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG, DIM_ENABLE_REFINEMENTS_FLAG,DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG, MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE, LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,ATTR_VALUE_SET_FLAG, VALUE_SET_NAME,ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME)\n', EEE_SQL_TEST.insert_attr.sql[EEE_SQL_TEST.insert])
		self.assertEqual("(204,'accounting_date','mdex:string',1,'2.3','MSI','N','N','N','N','N','N','N','0',0,SYSDATE,0,SYSDATE,0,null,null,null,null,null,null);", EEE_SQL_TEST.insert_attr.sql[EEE_SQL_TEST.values])


# 	def test_Insert_attribute_create_sql(self):
# 		self.assertEqual("""SET DEFINE OFF;
# REM INSERTING into APPS.FND_EID_PDR_ATTRS_B
# Insert into APPS.FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE, EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG, DIM_ENABLE_REFINEMENTS_FLAG,DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG, MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE, LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,ATTR_VALUE_SET_FLAG, VALUE_SET_NAME,ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME)
# COMMIT;""", EEE_SQL_TEST.insert_attr.sql)






if __name__ == '__main__':
	unittest.main()