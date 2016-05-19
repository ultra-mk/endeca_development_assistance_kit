import sys
import reader_writer
import sql_generator
import eql_generator
import xml_generator


def main(args=None):

	sql_reader_writer(reader_writer.Excel_Reader(), reader_writer.Text_Writer('sql.txt'))

	eql_reader_writer(reader_writer.Excel_Reader(), reader_writer.Text_Writer('eql.txt'),)

	# print '------------------------------------------------------------'
	# print 'now writing your XML file...........'
	# xml_writer = reader_writer.Text_Writer('xml.txt')
	# xml_writer.clear_file()
	# xml = xml_generator.XML({'test' : 'dict'}, 'receiving')
	# xml_writer.save_text(xml.file)
	# print 'beep, boop your XML is ready as well!'


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

if __name__ == '__main__':
	main()
