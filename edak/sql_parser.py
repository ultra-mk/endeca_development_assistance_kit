import os

class SQL_PARSER(object):


	def __init__(self, sql_file_name):
		self.sql_file_name = sql_file_name


	def check_for_file(self):
		return os.path.isfile(self.sql_file_name)


	def open_file(self):
		with open(self.sql_file_name) as f:
			lines = f.read().splitlines()
			return lines

	def find_from_index(self, sql_lines):
		for index, line in enumerate(sql_lines):
			if 'FROM' in line:
				return index

	def get_selected_columns(self,sql_lines, index_of_from):
		return [i.strip().replace(',','') for i in sql_lines[1:index_of_from] if len(i) > 0]