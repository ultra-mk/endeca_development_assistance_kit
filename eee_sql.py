
DEFINE_OFF = 'SET DEFINE OFF;\n'
COMMIT = 'COMMIT;'


class Insert_attribute(object):

    def __init__(self, eid_instance_id, eid_instance_attribute, datatype, profile_id):
		self.eid_instance_id = str(eid_instance_id)
		self.eid_instance_attribute = eid_instance_attribute
		self.datatype = datatype
		self.profile_id = str(profile_id)
		self.sql = self.create_sql(self.eid_instance_id, self.eid_instance_attribute, self.datatype, self.profile_id)

    def create_sql(self, eid_instance_id, eid_instance_attribute, datatype, profile_id):
    	rem_insert_statment = 'REM INSERTING into APPS.FND_EID_PDR_ATTRS_B\n'
    	insert_statement = 'Insert into APPS.FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE, EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG, DIM_ENABLE_REFINEMENTS_FLAG,DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG, MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE, LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,ATTR_VALUE_SET_FLAG, VALUE_SET_NAME,ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME)\n'
    	values =  "("+ eid_instance_id +",'" + eid_instance_attribute + "','" + datatype + "'," + profile_id + ",'2.3','MSI','N','N','N','N','N','N','N','0',0,SYSDATE,0,SYSDATE,0,null,null,null,null,null,null);\n"
    	statement = DEFINE_OFF + rem_insert_statment + insert_statement + values + COMMIT
    	return statement





# values (204,'accounting_date','mdex:string',1,'2.3','MSI','N','N','N','N','N','N','N','0',0,SYSDATE,0,SYSDATE,0,null,null,null,null,null,null);
		# statement = DEFINE_OFF + COMMIT
		# return statement



# ia = Insert_attribute(204,'accounting_date', 'mdex:string')

# print ia.sql

# REM INSERTING into APPS.FND_EID_PDR_ATTRS_B
# -- DELETE FROM APPS.FND_EID_PDR_ATTRS_B WHERE EID_INSTANCE_ID = '%s' AND EID_INSTANCE_ATTRIBUTE = 'accounting_date'
# Insert into APPS.FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE,EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG,DIM_ENABLE_REFINEMENTS_FLAG,DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG,MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,ATTR_VALUE_SET_FLAG,VALUE_SET_NAME,ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME) values (204,'accounting_date','mdex:string',1,'2.3','MSI','N','N','N','N','N','N','N','0',0,SYSDATE,0,SYSDATE,0,null,null,null,null,null,null);
