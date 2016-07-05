import unittest
from edak import reader_writer

class EXCEL_READER_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(EXCEL_READER_TEST):
		EXCEL_READER_TEST.reader = reader_writer.Excel_Reader('endeca_attributes.xlsx')

	def test_init(self):
		self.assertEqual("<class 'edak.reader_writer.Excel_Reader'>", str(type(EXCEL_READER_TEST.reader)))


class TEXT_WRITER_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(TEXT_WRITER_TEST):
		TEXT_WRITER_TEST.writer = reader_writer.Text_Writer('test_attribute_sql.txt')

	def test_init(self):
		self.assertEqual("<class 'edak.reader_writer.Text_Writer'>", str(type(TEXT_WRITER_TEST.writer)))


if __name__ == '__main__':
	unittest.main()