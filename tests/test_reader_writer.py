import unittest
from edak import reader_writer as r

class EEE_EXCEL_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(EEE_EXCEL_TEST):
		EEE_EXCEL_TEST.reader = r.Excel_Reader()

	def test_init(self):
		self.assertEqual("<class 'reader_writer.Excel_Reader'>", str(type(EEE_EXCEL_TEST.reader)))


class EEE_TEXT_WRITER(unittest.TestCase):

	@classmethod
	def setUpClass(EEE_TEXT_WRITER):
		EEE_TEXT_WRITER.writer = r.Text_Writer('test_attribute_sql.txt')

	def test_init(self):
		self.assertEqual("<class 'reader_writer.Text_Writer'>", str(type(EEE_TEXT_WRITER.writer)))


if __name__ == '__main__':
	unittest.main()