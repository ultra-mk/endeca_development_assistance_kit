class XML(object):
	CLOSE_XML = '\n</Record>\n</Metadata>'

	def __init__(self, field_dictionary, record_name):
		self.file = self.create_xml(self.create_metadata_id(id(self)), self.create_record_id(record_name), self.create_all_fields(field_dictionary), XML.CLOSE_XML)


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


	def create_xml(self, metadata_id, record_id, fields, CLOSE_XML):
		return metadata_id + record_id + fields + XML.CLOSE_XML


