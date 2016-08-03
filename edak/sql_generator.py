import table_data as td

class SQL(object):
    ALTER_SESSION = 'ALTER SESSION SET CURRENT_SCHEMA = APPS;'
    DEFINE_OFF = 'SET DEFINE OFF;\n'
    EBS_LANGUAGE_CODES = ('D', 'DK', 'E', 'F', 'NL',
                          'PT', 'PTB', 'S', 'US', 'ZHS')
    INSERT_INTO = 'Insert into '
    GROUP_NAME = 'Categories'

    def __init__(self, eid_instance_id, eid_instance_attribute, datatype, profile_id, display_name):
        self.eid_instance_id = str(eid_instance_id)
        self.eid_instance_attribute = eid_instance_attribute
        self.display_name = display_name
        self.datatype = datatype
        self.profile_id = str(profile_id)
        self.attrs_b_values = [self.eid_instance_id, self.eid_instance_attribute, self.datatype,
                               self.profile_id, '2.3', 'MSI', 'N', 'N', 'N', 'N',
                               'N', 'N', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0',
                               'null', 'null', 'null', 'null', 'null', 'null']

        self.attrs_tl_values = self.create_attrs_tl_values(
            str(eid_instance_id), eid_instance_attribute, display_name)

        self.attrs_group_values = [self.eid_instance_id, SQL.GROUP_NAME, self.eid_instance_attribute, '1',
                                   '1', 'MSI', '2.3', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0']

    def insert_single_attr(self, values, table, columns):
        return self.create_insert_statement(table, columns) + self.create_values_string(*values)

    def create_attrs_tl_values(self, eid_instance_id, eid_instance_attribute, display_name):
        return [[eid_instance_id, eid_instance_attribute, l, 'US',
                 display_name, display_name, display_name, display_name, '0',
                 'SYSDATE', '0', 'SYSDATE', '0'] for l in SQL.EBS_LANGUAGE_CODES]

    def insert_attrs_tl(self, eid_instance_id, eid_instance_attribute, language_code, display_name, table):
        values = [eid_instance_id, eid_instance_attribute, language_code, 'US', display_name,
                  display_name, display_name, display_name, '0', 'SYSDATE', '0', 'SYSDATE', '0']
        insert_statement = self.create_insert_statement(
            td.ATTRS_TL['name'], td.ATTRS_TL['columns'])
        return insert_statement + self.create_values_string(*values)

    def insert_attrs_tl_all(self, eid_instance_id, eid_instance_attribute, display_name, table):
        return ''.join([self.insert_attrs_tl(
            eid_instance_id, eid_instance_attribute, l, display_name, table) + '\n' for l in SQL.EBS_LANGUAGE_CODES])

    def update_attr_groups(self):
        update = 'UPDATE ' + td.ATTR_GROUPS['name'] + ' '
        set_statement = "SET EID_INSTANCE_GROUP_ATTR_SEQ = 1, EID_INST_GROUP_ATTR_USER_SEQ = 1 WHERE EID_INSTANCE_ID = " + \
            self.eid_instance_id + " AND EID_INSTANCE_ATTRIBUTE = '" + \
            self.eid_instance_attribute + "'; \n"
        return update + set_statement + '\n'

    def create_insert_statement(self, table, *args):
        return SQL.INSERT_INTO + table + ' (' + ','.join(*args) + ')\n'

    def create_values_string(self, *args):
        return 'values ( ' + ','.join([a if a in ['null', 'SYSDATE'] else a if a.isdigit() else "'" + a + "'" for a in args]) + ');'

    def generate_sql(self):
        return SQL.DEFINE_OFF + self.insert_single_attr(self.attrs_b_values, td.ATTRS_B['name'], td.ATTRS_B['columns']) + '\n' + self.insert_attrs_tl_all(
            self.eid_instance_id, self.eid_instance_attribute, self.display_name, td.ATTRS_TL['name']) + '\n' + self.insert_single_attr(self.attrs_group_values, td.ATTR_GROUPS['name'], td.ATTR_GROUPS['columns']) + '\n' + self.update_attr_groups()
