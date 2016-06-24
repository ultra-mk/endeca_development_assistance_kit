class EQL(object):

    def __init__(self, eid_instance_attributes, view_name):
        self.eid_instance_attributes = eid_instance_attributes
        self.view_name = view_name

    def define_as_clause(self):
    	return 'Define {} as SELECT \n'.format(self.view_name)

    def generate_eql(self):
        return self.define_as_clause() + ''.join([a + ' ' + 'as' + ' "' + a + '",' + ' \n' for a in self.eid_instance_attributes])
