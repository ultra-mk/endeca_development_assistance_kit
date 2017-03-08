import table_data as td


class SQL(object):
    LANGUAGES = ('D','DK', 'E', 'F', 'NL', 'PT', 'PTB', 'S', 'US', 'ZHS')

    def __init__(self, eid_instance_id, eid_instance_attribute, datatype, profile_id, display_name, sequence_number, group_name):
        self.eid_instance_id = str(eid_instance_id)
        self.sequence_number = str(sequence_number)
        self.profile_id = str(profile_id)
        self.eid_instance_attribute = eid_instance_attribute
        self.datatype = datatype
        self.display_name = display_name
        self.sequence_number = sequence_number
        self.group_name = group_name

    def attr_b(self, table, values):
        return ''.join(['Insert into ', table['name'], ' (',','.join(table['columns']), ')', '\nvalues ( ', ','.join(self._format_value(v) for v in values),');'])

    def attr_tl(self, table, values):
        return '\n'.join([self.attr_b(table, v) for v in values])

    def update_sequence(self):
        return ''.join(['UPDATE ', td.ATTR_GROUPS['name'], ' ', ''.join(self.sequence), '\n'])

    def build_sql(self, *args):
        return '\n'.join(*args)

    def _format_value(self, element):
        if element in ['null', 'SYSDATE'] or element.isdigit():
            return element
        else:
            return "'" + element + "'"
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
                 'SYSDATE', '0', 'SYSDATE', '0'] for l in SQL.LANGUAGES]

    @property
    def attrs_group(self):
        return [self.eid_instance_id, self.group_name, self.eid_instance_attribute, '1',
                '1', 'MSI', '2.3', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0']

    @property
    def sequence(self):
        return ["SET EID_INSTANCE_GROUP_ATTR_SEQ = {0}, EID_INST_GROUP_ATTR_USER_SEQ = {0} WHERE EID_INSTANCE_ID = ".format(self.sequence_number),
                self.eid_instance_id, " AND EID_INSTANCE_ATTRIBUTE = '", self.eid_instance_attribute, "';"]

    @property
    def groups_b(self):
        return [self.eid_instance_id, self.group_name, '2.3',
                '1', '1', 'MSI', 'N', '0', '0', 'SYSDATE', '0', 'SYSDATE', '0']

    @property
    def groups_tl(self):
        return [[self.eid_instance_id, self.group_name, l, 'US', self.group_name, self.group_name, self.group_name, self.group_name,
                 '0', 'SYSDATE', '0', 'SYSDATE', '0'] for l in SQL.LANGUAGES]

