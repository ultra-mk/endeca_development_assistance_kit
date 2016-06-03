class EQL(object):
	DEFINE_AS = 'Define view_name as SELECT \n' 

	def __init__(self, eid_instance_attributes):
		self.eid_instance_attributes = eid_instance_attributes


	def generate_eql(self):
		return EQL.DEFINE_AS + ''.join([a + ' ' +'as' +' "'+a+'",' +' \n' for a in self.eid_instance_attributes])
