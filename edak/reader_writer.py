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
		self.create_excel_file()

#naive implementation
	def create_excel_file(self):
		wb = openpyxl.Workbook()
		ws = wb.active
		ws.title = 'endeca_attributes'
		ws['A1'].value ='eid_instance_id'
		ws['B1'].value = 'eid_instance_attribute'
		ws['C1'].value = 'datatype'
		ws['D1'].value = 'profile_id'
		ws['E1'].value = 'display_name'
		wb.save(self.file_name)


class Text_Writer(object):

	def __init__(self, file):
		self.file = file


	def clear_file(self):
		open(self.file, 'w').close()


	def save_text(self, text):
		with open(self.file, 'a') as f:
			f.write(text)



