class XML(object):
	#want to move away from metadata_id and record_id being hardcoded
	METADATA_ID = '<Metadata id="Metadata18" previewAttachmentCharset="ISO-8859-1">\n'
	RECORD_ID = '<Record fieldDelimiter="|" name="receiving" previewAttachmentCharset="ISO-8859-1" recordDelimiter="\r\n" recordSize="-1" type="delimited">\n'
	CLOSE_XML = '\n</Record>\n</Metadata>'

	def __init__(self, field_dictionary):
		self.fields = self.create_all_fields(field_dictionary)
		self.file = self.create_xml()

	def create_single_field(self, attribute_name, datatype):
		return '<Field name="'+attribute_name+'" type="'+datatype+'"/>'


	def create_all_fields(self, field_dictionary):
		fields = []
		for key, value in field_dictionary.items():
			fields.append(self.create_single_field(key, value))
		return '\n'.join(fields)


	def create_xml(self):
		return XML.METADATA_ID + XML.RECORD_ID + self.fields + XML.CLOSE_XML

