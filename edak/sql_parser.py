import os

class SQL_PARSER(object):


	def __init__(self, sql_file_name):
		self.column_names = ['1','2','3']
		self.sql_file_name = sql_file_name


	def check_for_file():
		return os.path.isfile(self.sql_file_name)