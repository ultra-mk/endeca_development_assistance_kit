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


	def remove_table_names(self, selected_column_lines):
		return [item[item.index('.') + 1:] for item in selected_column_lines]


	def format_column_aliases(self, selected_column_lines):
		return [item[item.index(' AS ') + 4:] if ' AS ' in item else item for item in selected_column_lines]


	def parse_sql_file(self):
		if self.check_for_file():
			raw_sql_lines = self.open_file()
			from_index = self.find_from_index(raw_sql_lines)
			sql_lines = self.get_selected_columns(raw_sql_lines, from_index)
			sql_lines = self.remove_table_names(sql_lines)
			sql_lines = self.format_column_aliases(sql_lines)
			return sql_lines
		else:
			print 'file is not found'