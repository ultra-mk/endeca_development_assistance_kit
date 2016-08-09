import openpyxl


class Excel_Reader(object):

    def __init__(self, file_name):
        wb = openpyxl.load_workbook(file_name)
        sheet = wb.get_sheet_by_name('endeca_attributes')
        highest_row = str(sheet.get_highest_row())
        self.attribute_data = [[c.value for c in rowOfCellObjects]
                               for rowOfCellObjects in sheet['A2':'E' + highest_row]]
        self.eql_attributes = [i[1] for i in self.attribute_data]
        self.xml_attributes = [[i[1], i[2]] for i in self.attribute_data]


class Excel_Writer(object):

    def __init__(self, file_name, columns_and_datatype):
        self.file_name = file_name
        self.columns_and_datatype = columns_and_datatype
        self.create_excel_file()

# naive implementation
    def create_excel_file(self):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'endeca_attributes'
        ws['A1'].value = 'eid_instance_id'
        ws['B1'].value = 'eid_instance_attribute'
        ws['C1'].value = 'datatype'
        ws['D1'].value = 'profile_id'
        ws['E1'].value = 'display_name'
        for i, e in enumerate(self.columns_and_datatype):
            ws.cell(row=i + 2, column=2).value = e[0]
            ws.cell(row=i + 2, column=3).value = e[1]
        wb.save(self.file_name)


class Text_Writer(object):

    def __init__(self, file):
        self.file = file

    def clear_file(self):
        open(self.file, 'w').close()

    def save_text(self, text):
        with open(self.file, 'a') as f:
            f.write(text)
