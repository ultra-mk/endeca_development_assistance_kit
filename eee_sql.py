
DEFINE_OFF = 'SET DEFINE OFF;\n'
COMMIT = 'COMMIT;'


class SQL(object):


    def __init__(self, eid_instance_id, eid_instance_attribute, datatype, profile_id, display_name):
		self.eid_instance_id = str(eid_instance_id)
		self.eid_instance_attribute = eid_instance_attribute
		self.datatype = datatype
		self.profile_id = str(profile_id)
		self.display_name = display_name
		self.insert_attrs_b = self.insert_attrs_b(self.eid_instance_id, self.eid_instance_attribute, self.datatype, self.profile_id)
		self.insert_attrs_tl_all = self.insert_attrs_tl_all(self.eid_instance_id, self.eid_instance_attribute, self.display_name)

    def insert_attrs_b(self, eid_instance_id, eid_instance_attribute, datatype, profile_id):
    	rem_insert_statment = 'REM INSERTING into APPS.FND_EID_PDR_ATTRS_B\n'
    	insert_statement = 'Insert into APPS.FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE, EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG, DIM_ENABLE_REFINEMENTS_FLAG,DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG, MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE, LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,ATTR_VALUE_SET_FLAG, VALUE_SET_NAME,ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME)\n'
    	values =  "("+ eid_instance_id +",'" + eid_instance_attribute + "','" + datatype + "'," + profile_id + ",'2.3','MSI','N','N','N','N','N','N','N','0',0,SYSDATE,0,SYSDATE,0,null,null,null,null,null,null);\n"
    	statement = DEFINE_OFF + rem_insert_statment + insert_statement + values + COMMIT
    	return statement


    def insert_attrs_tl(self, eid_instance_id ,eid_instance_attribute, language_code, display_name):
    	insert_statement = 'Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values'
    	values = "(" + eid_instance_id + ",'"+eid_instance_attribute+"','" + language_code + "','US','" + display_name + "','" + display_name +"','" + display_name + "','" + display_name + "',0,SYSDATE,0,SYSDATE,0);" 
    	statement = insert_statement + values 
    	return statement

    def insert_attrs_tl_all(self, eid_instance_id, eid_instance_attribute, display_name):
    	ebs_language_codes = ('D', 'DK', 'E', 'F', 'NL', 'PT', 'PTB', 'S', 'US', 'ZHS')
        rem_insert_statement = 'REM INSERTING into APPS.FND_EID_PDR_ATTRS_TL\n'
        statement = DEFINE_OFF + rem_insert_statement
        for l in ebs_language_codes:
        	language_statement = self.insert_attrs_tl(eid_instance_id, eid_instance_attribute, l, display_name)
        	statement += language_statement + '\n'
        return statement + '\n' + COMMIT 




