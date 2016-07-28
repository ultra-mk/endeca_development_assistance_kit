
class SQL(object):
    ALTER_SESSION = 'ALTER SESSION SET CURRENT_SCHEMA = APPS;'
    DEFINE_OFF = 'SET DEFINE OFF;\n'
    COMMIT = 'COMMIT;'
    EBS_LANGUAGE_CODES = ('D', 'DK', 'E', 'F', 'NL',
                          'PT', 'PTB', 'S', 'US', 'ZHS')
    REM_INSERT = 'REM INSERTING into '
    INSERT_INTO = 'Insert into '
    ATTRS_B = {'name': 'FND_EID_PDR_ATTRS_B', 'columns': ['EID_INSTANCE_ID', 'EID_INSTANCE_ATTRIBUTE', 'ENDECA_DATATYPE',
                                                          'EID_ATTR_PROFILE_ID', 'EID_RELEASE_VERSION', 'ATTRIBUTE_SOURCE',
                                                          'MANAGED_ATTRIBUTE_FLAG', 'HIERARCHICAL_MGD_ATTR_FLAG',
                                                          'DIM_ENABLE_REFINEMENTS_FLAG', 'DIM_SEARCH_HIERARCHICAL_FLAG',
                                                          'REC_SEARCH_HIERARCHICAL_FLAG', 'MGD_ATTR_EID_RELEASE_VERSION',
                                                          'OBSOLETED_FLAG', 'OBSOLETED_EID_RELEASE_VERSION,CREATED_BY',
                                                          'CREATION_DATE', 'LAST_UPDATED_BY', 'LAST_UPDATE_DATE',
                                                          'LAST_UPDATE_LOGIN', 'ATTR_ENABLE_UPDATE_FLAG', 'VIEW_OBJECT_ATTR_NAME',
                                                          'ATTR_VALUE_SET_FLAG', 'VALUE_SET_NAME', 'ATTR_ENABLE_NULL_FLAG',
                                                          'DESCRIPTIVE_FLEXFIELD_NAME']}

    ATTRS_TL = {'name': 'FND_EID_PDR_ATTRS_TL', 'columns': ['EID_INSTANCE_ID', 'EID_INSTANCE_ATTRIBUTE','LANGUAGE',
                                                            'SOURCE_LANG', 'DISPLAY_NAME', 'ATTRIBUTE_DESC',
                                                            'USER_DISPLAY_NAME', 'USER_ATTRIBUTE_DESC,CREATED_BY',
                                                            'CREATION_DATE', 'LAST_UPDATED_BY', 'LAST_UPDATE_DATE',
                                                            'LAST_UPDATE_LOGIN']}

    ATTR_GROUPS = {'name':'FND_EID_ATTR_GROUPS', 'columns' : ['EID_INSTANCE_ID', 'EID_INSTANCE_GROUP', 'EID_INSTANCE_ATTRIBUTE', 
                                                              'EID_INSTANCE_GROUP_ATTR_SEQ', 'EID_INST_GROUP_ATTR_USER_SEQ', 
                                                              'GROUP_ATTRIBUTE_SOURCE','EID_RELEASE_VERSION', 'OBSOLETED_FLAG', 
                                                              'OBSOLETED_EID_RELEASE_VERSION', 'CREATED_BY', 'CREATION_DATE', 
                                                              'LAST_UPDATED_BY', 'LAST_UPDATE_DATE', 'LAST_UPDATE_LOGIN']}
    GROUP_NAME = 'Categories'

    def __init__(self, eid_instance_id, eid_instance_attribute, datatype, profile_id, display_name):
        self.insert_attrs_b = self.insert_attrs_b(str(
            eid_instance_id), eid_instance_attribute, datatype, str(profile_id), SQL.ATTRS_B['name'])
        self.insert_attrs_tl_all = self.insert_attrs_tl_all(
            str(eid_instance_id), eid_instance_attribute, display_name, SQL.ATTRS_TL['name'])
        self.insert_attr_groups = self.insert_attr_groups(
            str(eid_instance_id), eid_instance_attribute, SQL.ATTR_GROUPS['name'])
        self.update_attr_groups = self.update_attr_groups(
            str(eid_instance_id), eid_instance_attribute, SQL.ATTR_GROUPS['name'])

        self.attrs_b_values = [str(eid_instance_id), eid_instance_attribute, datatype, 
                            str(profile_id), '2.3', 'MSI', 'N', 'N', 'N', 'N',
                            'N', 'N', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0', 
                            'null', 'null', 'null', 'null', 'null', 'null']

    def insert_single_attr(self, values, table, columns):
        return self.create_insert_statement(table, columns) + self.create_values_string(*values)


    def insert_attrs_b(self, eid_instance_id, eid_instance_attribute, datatype, profile_id, table):
        values = [eid_instance_id, eid_instance_attribute, datatype, profile_id, '2.3', 'MSI', 'N', 'N', 'N', 'N',
                  'N', 'N', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0', 'null', 'null', 'null', 'null', 'null', 'null']
        insert_statement = self.create_insert_statement(
            SQL.ATTRS_B['name'], SQL.ATTRS_B['columns'])
        return insert_statement + self.create_values_string(*values)


    def insert_attrs_tl(self, eid_instance_id, eid_instance_attribute, language_code, display_name, table):
        values = [eid_instance_id, eid_instance_attribute, language_code, 'US', display_name,
                  display_name, display_name, display_name, '0', 'SYSDATE', '0', 'SYSDATE', '0']
        insert_statement = self.create_insert_statement(SQL.ATTRS_TL['name'], SQL.ATTRS_TL['columns'])
        return insert_statement + self.create_values_string(*values)

    def insert_attrs_tl_all(self, eid_instance_id, eid_instance_attribute, display_name, table):
        statement = SQL.DEFINE_OFF + SQL.REM_INSERT + table + '\n'
        language_statement = [self.insert_attrs_tl(
            eid_instance_id, eid_instance_attribute, l, display_name, table) + '\n' for l in SQL.EBS_LANGUAGE_CODES]
        statement = statement + ''.join(language_statement)
        return statement + '\n' + SQL.COMMIT

    def insert_attr_groups(self, eid_instance_id, eid_instance_attribute, table):
        rem_insert_statement = SQL.REM_INSERT + table + '\n'
        values = [eid_instance_id, SQL.GROUP_NAME, eid_instance_attribute, '1',
                  '1', 'MSI', '2.3', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0']
        insert_statement = self.create_insert_statement(
            SQL.ATTR_GROUPS['name'], SQL.ATTR_GROUPS['columns'])
        return SQL.DEFINE_OFF + rem_insert_statement + insert_statement + self.create_values_string(*values) + SQL.COMMIT

    def update_attr_groups(self, eid_instance_id, eid_instance_attribute, table):
        update = 'UPDATE ' + table + ' '
        set_statement = "SET EID_INSTANCE_GROUP_ATTR_SEQ = 1, EID_INST_GROUP_ATTR_USER_SEQ = 1 WHERE EID_INSTANCE_ID = " + \
            eid_instance_id + " AND EID_INSTANCE_ATTRIBUTE = '" + \
            eid_instance_attribute + "'; \n"
        return SQL.DEFINE_OFF + update + set_statement + SQL.COMMIT + '\n'

    def create_insert_statement(self, table, column_headers):
        return SQL.INSERT_INTO + table + self.create_column_name_string(*column_headers)

    def create_column_name_string(self, *args):
        statement = ' (' + ''.join([a + ',' for a in args])
        statement = statement[0:-1]
        return statement + ')\n'

    def create_values_string(self, *args):
        statement = 'values ( '
        for a in args:
            if a == 'null' or a == 'SYSDATE' or a.isdigit():
                statement += a + ','
            else:
                statement += "'" + a + "'" + ','
        statement = statement[0:-1]
        return statement + ');'

    def generate_sql(self):
        return SQL.DEFINE_OFF + self.insert_attrs_b + '\n' + self.insert_attrs_tl_all + '\n' + self.insert_attr_groups + '\n' + self.update_attr_groups
