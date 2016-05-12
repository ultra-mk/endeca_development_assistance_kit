import unittest
from edak import xml_generator as x

class XML_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(XML_TEST):
		XML_TEST.xml = x.XML({'currency_code': 'string', 'organization_id':'string'},'receiving')
		XML_TEST.metadata_id = id(XML_TEST.xml)
		XML_TEST.XML_FILE = '<Metadata id="'+str(XML_TEST.metadata_id)+'" previewAttachmentCharset="ISO-8859-1">\n<Record fieldDelimiter="|" name="receiving" previewAttachmentCharset="ISO-8859-1" recordDelimiter="\r\n" recordSize="-1" type="delimited">\n<Field name="organization_id" type="string"/>\n<Field name="currency_code" type="string"/>\n</Record>\n</Metadata>'
		XML_TEST.record_name = 'receiving'


	def test_create_metadata_id(self):
		self.assertEqual('<Metadata id="{}" previewAttachmentCharset="ISO-8859-1">\n'.format(XML_TEST.metadata_id), XML_TEST.xml.create_metadata_id(XML_TEST.metadata_id))


	def test_close_xml(self):
		self.assertEqual("\n</Record>\n</Metadata>", XML_TEST.xml.CLOSE_XML)


	def test_create_record_id(self):
		self.assertEqual('<Record fieldDelimiter="|" name="receiving" previewAttachmentCharset="ISO-8859-1" recordDelimiter="\r\n" recordSize="-1" type="delimited">\n', XML_TEST.xml.create_record_id(XML_TEST.record_name))

	def test_create_single_field(self):
		self.assertEqual('<Field name="po_header_id" type="string"/>', XML_TEST.xml.create_single_field('po_header_id', 'string'))


	def test_create_all_fields(self):
		self.assertEqual('<Field name="organization_id" type="string"/>\n<Field name="currency_code" type="string"/>', XML_TEST.xml.fields)


	def test_create_xml(self):
		self.assertEqual(XML_TEST.XML_FILE, XML_TEST.xml.file)
