import unittest
from edak import xml_generator as x

class XML_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(XML_TEST):
		XML_TEST.fields = {'currency_code': 'string', 'organization_id':'string'}
		XML_TEST.record_name = 'receiving'
		XML_TEST.xml = x.XML(XML_TEST.fields,XML_TEST.record_name)
		XML_TEST.metadata_id = id(XML_TEST.xml)
		XML_TEST.XML_FILE = '<Metadata id="'+str(XML_TEST.metadata_id)+'" previewAttachmentCharset="ISO-8859-1">\n<Record fieldDelimiter="|" name="receiving" previewAttachmentCharset="ISO-8859-1" recordDelimiter="\r\n" recordSize="-1" type="delimited">\n<Field name="organization_id" type="string"/>\n<Field name="currency_code" type="string"/>\n</Record>\n</Metadata>'


	def test_metadata_id(self):
		self.assertEqual('<Metadata id="{}" previewAttachmentCharset="ISO-8859-1">\n'.format(XML_TEST.metadata_id), XML_TEST.xml.metadata_id(XML_TEST.metadata_id))


	def test_close_xml(self):
		self.assertEqual("\n</Record>\n</Metadata>", XML_TEST.xml.CLOSE_XML)


	def test_record_id(self):
		self.assertEqual('<Record fieldDelimiter="|" name="receiving" previewAttachmentCharset="ISO-8859-1" recordDelimiter="\r\n" recordSize="-1" type="delimited">\n', XML_TEST.xml.record_id(XML_TEST.record_name))

	def test_single_field(self):
		self.assertEqual('<Field name="po_header_id" type="string"/>', XML_TEST.xml.single_field('po_header_id', 'string'))


	def test_all_fields(self):
		self.assertEqual('<Field name="organization_id" type="string"/>\n<Field name="currency_code" type="string"/>', XML_TEST.xml.all_fields(XML_TEST.fields))


	def test_xml(self):
		self.assertEqual(XML_TEST.XML_FILE, XML_TEST.xml.file)