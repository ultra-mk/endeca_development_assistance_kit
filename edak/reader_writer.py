import openpyxl


class Excel_Reader(object):

	def __init__(self, file_name):
		wb = openpyxl.load_workbook(file_name)
		sheet = wb.get_sheet_by_name('endeca_attributes')
		highest_row = str(sheet.get_highest_row())
		self.attribute_data = [[c.value for c in rowOfCellObjects] for rowOfCellObjects in sheet['A2':'E'+highest_row]]

#UUUUGHHHHHHHHHHHHH
# this puts the quick and dirty into quick and dirty

		self.eql_attributes = []
		for col in sheet.columns[1]:
			self.eql_attributes.append(col.value)
		del self.eql_attributes[0]

		self.xml_attributes = [[c.value for c in rowOfCellObjects] for rowOfCellObjects in sheet['B2':'C'+highest_row]]

class Excel_Writer(object):

	def __init__(self):
		self.file_name = 'excel_writer_test.xlsx'


	def save_files(self):
		wb.save(self.file_name)


class Text_Writer(object):

	def __init__(self, file):
		self.file = file


	def clear_file(self):
		open(self.file, 'w').close()


	def save_text(self, text):
		with open(self.file, 'a') as f:
			f.write(text)



