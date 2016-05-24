import sys
import reader_writer
import sql_generator
import eql_generator
import xml_generator


def main(args=None):

	sql_reader_writer(reader_writer.Excel_Reader(), reader_writer.Text_Writer('sql.txt'))

	eql_reader_writer(reader_writer.Excel_Reader(), reader_writer.Text_Writer('eql.txt'))

	xml_reader_writer(reader_writer.Excel_Reader(), reader_writer.Text_Writer('xml.txt'))


def sql_reader_writer(reader, writer):
	print 'writing some sweet PLSQL for you........'
	reader = reader
	writer = writer
	writer.clear_file()
	for r in reader.attribute_data:
		sql = sql_generator.SQL(*r)
		writer.save_text(sql.file)
	print 'beep, boop your PLSQL is ready!'

def eql_reader_writer(reader, writer):
	print 'writing some sweet EQL for you...........'
	reader = reader
	writer = writer
	writer.clear_file()
	writer.save_text(eql_generator.EQL(reader.attribute_names).generate_EQL())
	print 'beep, boop, your EQL is ready!'

def xml_reader_writer(reader, writer):
	print 'writing some sweet XML for you'
	reader = reader
	writer = writer
	writer.clear_file()
	writer.save_text(xml_generator.XML(reader.attribute_dict, 'metadata1').file)
	print 'beep, boop your XML is ready'


if __name__ == '__main__':
	main()
