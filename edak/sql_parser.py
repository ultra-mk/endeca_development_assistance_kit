import os
import utils


class SQL_PARSER(object):

    def __init__(self, sql_file_name):
        self.sql_file_name = sql_file_name

    def find_from_index(self, sql_lines):
        for index, line in enumerate(sql_lines):
            if 'FROM ' in line:
                return index

    def get_selected_columns(self, sql_lines, index_of_from):
        return [i.strip().replace(',', '') for i in sql_lines[1:index_of_from] if len(i) > 0]

    def remove_table_names(self, selected_column_lines):
        return [item[item.index('.') + 1:] for item in selected_column_lines]

    def format_column_aliases(self, selected_column_lines):
        return [item[item.index(' AS ') + 4:] if ' AS ' in item else item for item in selected_column_lines]

    def parse_sql_file(self):
        if utils.check_for_file(self.sql_file_name):
            raw_sql_lines = utils.open_file_split_into_lines(
                self.sql_file_name)
            from_index = self.find_from_index(raw_sql_lines)
            sql_lines = self.get_selected_columns(raw_sql_lines, from_index)
            sql_lines = self.remove_table_names(sql_lines)
            sql_lines = self.format_column_aliases(sql_lines)
            return sql_lines
        else:
            print 'file is not found'

    def reduce_columns(self, columns, keyword):
        return [keyword if keyword in c else c for c in columns]

    def generate_endeca_datatypes(self, columns):
        data_type_translation = {'DATE': 'mdex:dateTime', 'AMOUNT': 'mdex:double',
                                 'QUANTITY': 'mdex:int', 'PRICE': 'mdex:double'}
    
        reduced = self.reduce_columns(columns, 'DATE')
        reduced = self.reduce_columns(reduced, 'AMOUNT')
        reduced = self.reduce_columns(reduced, 'QUANITY')
        reduced = self.reduce_columns(reduced, 'PRICE')
        return [data_type_translation[r] if r in data_type_translation else 'mdex:string' for r in reduced]
