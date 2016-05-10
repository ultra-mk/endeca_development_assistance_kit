import unittest
from edak import xml_generator as x

class XML_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(XML_TEST):
		XML_TEST.xml = x.XML()


	def test_metadata_id(self):
		self.assertEqual('<Metadata id="Metadata18" previewAttachmentCharset="ISO-8859-1">', XML_TEST.xml.METADATA_ID)


	def test_record_id(self):
		self.assertEqual('<Record fieldDelimiter="|" name="receiving" previewAttachmentCharset="ISO-8859-1" recordDelimiter="\r\n" recordSize="-1" type="delimited">', XML_TEST.xml.RECORD_ID)


	def test_close_xml(self):
		self.assertEqual("</Record>\n</Metadata>", XML_TEST.xml.CLOSE_XML)


	def test_create_field(self):
		self.assertEqual('<Field name="po_header_id" type="string"/>', XML_TEST.xml.create_field('po_header_id', 'string'))



