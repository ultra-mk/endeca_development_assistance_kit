import sys
import reader_writer
import sql_generator
import eql_generator
import xml_generator


def main(args=None):

	# sql_reader_writer(reader_writer.Excel_Reader('endeca_attributes_FIN_342.xlsx'), reader_writer.Text_Writer('sql.txt'))

	# eql_reader_writer(reader_writer.Excel_Reader('endeca_attributes_FIN_342.xlsx'), reader_writer.Text_Writer('eql.txt'))

	xml_reader_writer(reader_writer.Excel_Reader('endeca_attributes_FIN_342.xlsx'), reader_writer.Text_Writer('xml.txt'))


def sql_reader_writer(reader, writer):
	print 'writing some sweet PLSQL for you........'
	writer.clear_file()
	for r in reader.attribute_data:
		sql = sql_generator.SQL(*r)
		writer.save_text(sql.generate_sql())
	print 'beep, boop your PLSQL is ready!'

def eql_reader_writer(reader, writer):
	print 'writing some sweet EQL for you...........'
	writer.clear_file()
	writer.save_text(eql_generator.EQL(reader.attribute_names).generate_eql())
	print 'beep, boop, your EQL is ready!'

def xml_reader_writer(reader, writer):
	print 'writing some sweet XML for you'
	writer.clear_file()
	writer.save_text(xml_generator.XML(reader.xml_attributes, 'metadata1').generate_xml())
	print 'beep, boop your XML is ready'


if __name__ == '__main__':
	main()
