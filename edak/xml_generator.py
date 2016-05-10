class XML(object):
	METADATA_ID = '<Metadata id="Metadata18" previewAttachmentCharset="ISO-8859-1">'
	RECORD_ID = '<Record fieldDelimiter="|" name="receiving" previewAttachmentCharset="ISO-8859-1" recordDelimiter="\r\n" recordSize="-1" type="delimited">'
	CLOSE_XML = '</Record>\n</Metadata>'

	def __init__(self):
		self.stuff = 'attributes go here'


	def create_field(self, attribute_name, datatype):
		return '<Field name="'+attribute_name+'" type="'+datatype+'"/>'



