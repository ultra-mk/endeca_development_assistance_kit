import table_data as td


class SQL(object):
    DEFINE_OFF = 'SET DEFINE OFF;\n'
    EBS_LANGUAGE_CODES = ('D', 'DK', 'E', 'F', 'NL',
                          'PT', 'PTB', 'S', 'US', 'ZHS')
    INSERT_INTO = 'Insert into '

    def __init__(self, eid_instance_id, eid_instance_attribute, datatype, profile_id, display_name, sequence_number, group_name):
        self.eid_instance_id = str(eid_instance_id)
        self.sequence_number = str(sequence_number)
        self.profile_id = str(profile_id)
        self.attrs_b_values = [self.eid_instance_id, eid_instance_attribute, datatype,
                               self.profile_id, '2.3', 'MSI', 'N', 'N', 'N', 'N',
                               'N', 'N', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0',
                               'null', 'null', 'null', 'null', 'null', 'null']

        self.attrs_tl_values = [[self.eid_instance_id, eid_instance_attribute, l, 'US',
                                 display_name, display_name, display_name, display_name, '0',
                                 'SYSDATE', '0', 'SYSDATE', '0'] for l in SQL.EBS_LANGUAGE_CODES]

        self.attrs_group_values = [self.eid_instance_id, group_name, eid_instance_attribute, '1',
                                   '1', 'MSI', '2.3', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0']

        self.set_attr_groups = ["SET EID_INSTANCE_GROUP_ATTR_SEQ = {0}, EID_INST_GROUP_ATTR_USER_SEQ = {0} WHERE EID_INSTANCE_ID = ".format(self.sequence_number),
                                self.eid_instance_id, " AND EID_INSTANCE_ATTRIBUTE = '", eid_instance_attribute, "'; \n"]

        self.groups_b_values = [self.eid_instance_id, group_name, '2.3',
                                '1', '1', 'MSI', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0']

        self.groups_tl_values = [[self.eid_instance_id, group_name, l, 'US', group_name, group_name, group_name, group_name,
                                  '0', 'SYSDATE', '0', 'SYSDATE', '0'] for l in SQL.EBS_LANGUAGE_CODES]

    def attr_b(self, values, table, columns):
        return ''.join([self.insert_statement(table, columns), self.values_string(*values)])

    def attr_tl(self):
        return ''.join([self.attr_b(t, td.ATTRS_TL['name'], td.ATTRS_TL['columns']) + '\n' for t in self.attrs_tl_values])

    def attr_groups(self):
        update = ''.join(['UPDATE ', td.ATTR_GROUPS['name'], ' '])
        set_statement = ''.join(self.set_attr_groups)
        return ''.join([update, set_statement, '\n'])

    def insert_statement(self, table, *args):
        return SQL.INSERT_INTO + table + ' (' + ','.join(*args) + ')\n'

    def values_string(self, *args):
        return 'values ( ' + ','.join([a if a in ['null', 'SYSDATE'] else a if a.isdigit() else "'" + a + "'" for a in args]) + ');'

    def attr_sql(self):
        return ''.join([SQL.DEFINE_OFF, self.attr_b(self.attrs_b_values, td.ATTRS_B['name'],
                                                                td.ATTRS_B['columns']), '\n', self.attr_tl(), '\n',
                        self.attr_b(self.attrs_group_values, td.ATTR_GROUPS['name'],
                                                td.ATTR_GROUPS['columns']), '\n', self.attr_groups()])
    def groups_b_sql(self):
        return ''.join([self.attr_b(self.groups_b_values, td.GROUPS_B['name'],
                                                td.GROUPS_B['columns'])])

    def groups_tl_sql(self):
        return ''.join([self.attr_b(t, td.GROUPS_TL['name'],
                                                td.GROUPS_TL['columns']) + '\n' for t in self.groups_tl_values])
