class XML(object):
	CLOSE_XML = '\n</Record>\n</Metadata>'

	def __init__(self, field_dictionary, record_name):
		self.file = self.xml(self.metadata_id(id(self)), self.record_id(record_name), 
							 self.all_fields(field_dictionary), XML.CLOSE_XML)


	def metadata_id(self, metadata_id):
		return  '<Metadata id="{}" previewAttachmentCharset="ISO-8859-1">\n'.format(metadata_id)


	def record_id(self, record_name):
		return r'<Record fieldDelimiter="|" name="{}" previewAttachmentCharset="ISO-8859-1" recordDelimiter="\r\n" recordSize="-1" type="delimited">\n'.format(record_name)


	def single_field(self, attribute_name, datatype):
		return '<Field name="'+attribute_name+'" type="'+datatype+'"/>'


	def all_fields(self, field_dictionary):
		fields = []
		for key, value in field_dictionary.items():
			fields.append(self.single_field(key, value))
		return '\n'.join(fields)


	def xml(self, metadata_id, record_id, fields, CLOSE_XML):
		return metadata_id + record_id + fields + CLOSE_XML


