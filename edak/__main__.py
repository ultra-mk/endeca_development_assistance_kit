import sys
import sql_generator
import reader_writer
import eql_generator


def main(args=None):
	print 'writing some sweet PLSQL for you........'
	reader = reader_writer.Excel_Reader()
	sql_writer = reader_writer.Text_Writer('sql.txt')
	sql_writer.clear_file()
	for r in reader.attribute_data:
		sql = sql_generator.SQL(*r)
		sql_writer.save_text(sql.file)

	print 'beep, boop your PLSQL is ready!'
	print '------------------------------------------------------'
	print 'now writing some EQL for you..................................'
	eql_writer = reader_writer.Text_Writer('eql.txt') 
	eql = eql_generator.EQL(reader.attribute_names)
	eql_writer.save_text(eql.generate_EQL())
	print 'beep, boop your EQL is ready too!'


if __name__ == '__main__':
	main()


# reader = Excel_Reader()
# sql_writer = Text_Writer('attribute_sql.txt')

# sql_writer.clear_file()
# for r in reader.attribute_data:
# 	sql = SQL(*r)
# 	sql_writer.save_text(sql.insert_attrs_b + '\n' + sql.insert_attrs_tl_all + '\n' + sql.insert_attr_groups + '\n' + sql.update_attr_groups) 



# eql_writer = Text_Writer('eql.txt') 
# eql = EQL(reader.attribute_names)
# eql_writer.save_text(eql.generate_EQL())