class XML(object):
	CLOSE_XML = '\n</Record>\n</Metadata>'

	def __init__(self, field_dictionary, record_name):
		self.fields = self.create_all_fields(field_dictionary)
		self.record_id = self.create_record_id(record_name)
		self.metadata_id = self.create_metadata_id(id(self))
		self.file = self.create_xml()


	def create_metadata_id(self, metadata_id):
		return  '<Metadata id="{}" previewAttachmentCharset="ISO-8859-1">\n'.format(metadata_id)

	def create_record_id(self, record_name):
		return '<Record fieldDelimiter="|" name="{}" previewAttachmentCharset="ISO-8859-1" recordDelimiter="\r\n" recordSize="-1" type="delimited">\n'.format(record_name)


	def create_single_field(self, attribute_name, datatype):
		return '<Field name="'+attribute_name+'" type="'+datatype+'"/>'


	def create_all_fields(self, field_dictionary):
		fields = []
		for key, value in field_dictionary.items():
			fields.append(self.create_single_field(key, value))
		return '\n'.join(fields)


	def create_xml(self):
		return self.metadata_id + self.record_id + self.fields + XML.CLOSE_XML

