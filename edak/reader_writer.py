import openpyxl

class Excel_Reader(object):

	def __init__(self):
		wb = openpyxl.load_workbook('endeca_attributes.xlsx')
		sheet = wb.get_sheet_by_name('endeca_attributes')
		highest_row = str(sheet.get_highest_row())
		self.attribute_data = [[c.value for c in rowOfCellObjects] for rowOfCellObjects in sheet['A2':'E'+highest_row]]
# this puts the quick and dirty into quick and dirty
# 		self.attribute_names = []
# 		for col in sheet.columns[1]:
# 			self.attribute_names.append(col.value)
# 		del self.attribute_names[0]

class Text_Writer(object):

	def __init__(self, file):
		self.file = file


	def clear_file(self):
		open(self.file, 'w').close()


	def save_text(self, text):
		with open(self.file, 'a') as f:
			f.write(text)



# reader = Excel_Reader()
# sql_writer = Text_Writer('attribute_sql.txt')

# sql_writer.clear_file()
# for r in reader.attribute_data:
# 	sql = SQL(*r)
# 	sql_writer.save_text(sql.insert_attrs_b + '\n' + sql.insert_attrs_tl_all + '\n' + sql.insert_attr_groups + '\n' + sql.update_attr_groups) 



# eql_writer = Text_Writer('eql.txt') 
# eql = EQL(reader.attribute_names)
# eql_writer.save_text(eql.generate_EQL())