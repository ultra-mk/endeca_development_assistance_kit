import table_data as td


class SQL(object):
    LANGUAGE_CODES = ('D', 'DK', 'E', 'F', 'NL',
                      'PT', 'PTB', 'S', 'US', 'ZHS')

    def __init__(self, eid_instance_id, eid_instance_attribute, datatype, profile_id, display_name, sequence_number, group_name):
        self.eid_instance_id = str(eid_instance_id)
        self.sequence_number = str(sequence_number)
        self.profile_id = str(profile_id)
        self.eid_instance_attribute = eid_instance_attribute
        self.datatype = datatype
        self.display_name = display_name
        self.sequence_number = sequence_number
        self.group_name = group_name

    def attr_b(self, values, table, columns):
        return ''.join([self.insert_statement(table, columns), self.values(*values)])

    def attr_tl(self):
        return ''.join([self.attr_b(t, td.ATTRS_TL['name'], td.ATTRS_TL['columns']) + '\n' for t in self.attrs_tl])

    def attr_groups(self):
        update = ''.join(['UPDATE ', td.ATTR_GROUPS['name'], ' '])
        set_statement = ''.join(self.set_attr_groups)
        return ''.join([update, set_statement, '\n'])

    def insert_statement(self, table, *args):
        return 'Insert into ' + table + ' (' + ','.join(*args) + ')\n'

    def values(self, *args):
        return 'values ( ' + ','.join([a if a in ['null', 'SYSDATE'] else a if a.isdigit() else "'" + a + "'" for a in args]) + ');'

    def attr_sql(self):
        return ''.join(['SET DEFINE OFF;\n', self.attr_b(self.attrs_b, td.ATTRS_B['name'],
                                                         td.ATTRS_B['columns']), '\n', self.attr_tl(), '\n',
                        self.attr_b(self.attrs_group, td.ATTR_GROUPS['name'],
                                    td.ATTR_GROUPS['columns']), '\n', self.attr_groups()])

    def groups_b_sql(self):
        return ''.join([self.attr_b(self.groups_b, td.GROUPS_B['name'],
                                    td.GROUPS_B['columns'])])

    def groups_tl_sql(self):
        return ''.join([self.attr_b(t, td.GROUPS_TL['name'],
                                    td.GROUPS_TL['columns']) + '\n' for t in self.groups_tl])

    @property
    def attrs_b(self):
        return [self.eid_instance_id, self.eid_instance_attribute, self.datatype,
                self.profile_id, '2.3', 'MSI', 'N', 'N', 'N', 'N',
                'N', 'N', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0',
                'null', 'null', 'null', 'null', 'null', 'null']

    @property
    def attrs_tl(self):
        return [[self.eid_instance_id, self.eid_instance_attribute, l, 'US',
                 self.display_name, self.display_name, self.display_name, self.display_name, '0',
                 'SYSDATE', '0', 'SYSDATE', '0'] for l in SQL.LANGUAGE_CODES]

    @property
    def attrs_group(self):
        return [self.eid_instance_id, self.group_name, self.eid_instance_attribute, '1',
                '1', 'MSI', '2.3', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0']

    @property
    def set_attr_groups(self):
        return ["SET EID_INSTANCE_GROUP_ATTR_SEQ = {0}, EID_INST_GROUP_ATTR_USER_SEQ = {0} WHERE EID_INSTANCE_ID = ".format(self.sequence_number),
                self.eid_instance_id, " AND EID_INSTANCE_ATTRIBUTE = '", self.eid_instance_attribute, "'; \n"]

    @property
    def groups_b(self):
        return [self.eid_instance_id, self.group_name, '2.3',
                '1', '1', 'MSI', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0']

    @property
    def groups_tl(self):
        return [[self.eid_instance_id, self.group_name, l, 'US', self.group_name, self.group_name, self.group_name, self.group_name,
                 '0', 'SYSDATE', '0', 'SYSDATE', '0'] for l in SQL.LANGUAGE_CODES]
