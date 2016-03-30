
DEFINE_OFF = 'SET DEFINE OFF;\n'
COMMIT = 'COMMIT;'


class Insert_attribute(object):

	def __init__(self, eid_instance_id, eid_instance_attribute, datatype):
		self.eid_instance_id = eid_instance_id
		self.eid_instance_attribute = eid_instance_attribute
		self.datatype = datatype

	def create_sql(self):
		statement = DEFINE_OFF + COMMIT
		return statement
