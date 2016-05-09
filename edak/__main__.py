import sys
import sql_generator
import reader_writer


def main(args=None):
	print 'this is the start of the main method'
	reader = reader_writer.Excel_Reader()
	sql_writer = reader_writer.Text_Writer('attribute_sql.txt')
	sql_writer.clear_file()
	for r in reader.attribute_data:
		sql = sql_generator.SQL(*r)
		sql_writer.save_text(sql.insert_attrs_b + '\n' + sql.insert_attrs_tl_all + '\n' + sql.insert_attr_groups + '\n' + sql.update_attr_groups) 

	print 'this is the end of the main method'



if __name__ == '__main__':
	main()