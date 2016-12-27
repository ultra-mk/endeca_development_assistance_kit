import os
import utils
import datatype_dictionary as dd


class SQL_PARSER(object):

    def __init__(self, sql_file_name):
        self.sql_file_name = sql_file_name

    def find_index(self, sql_lines, search_item):
        for index, line in enumerate(sql_lines):
            if search_item in line:
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
            from_index = self.find_index(raw_sql_lines, 'FROM ')
            sql_lines = self.get_selected_columns(raw_sql_lines, from_index)
            sql_lines = self.remove_table_names(sql_lines)
            sql_lines = self.format_column_aliases(sql_lines)
            return sql_lines
        else:
            print 'file is not found'

    def generate_endeca_datatypes(self, columns):
        return [[c, dd.ORACLE_COLUMNS_TO_ENDECA[c] if c in dd.ORACLE_COLUMNS_TO_ENDECA else 'mdex:string'] for c in columns]

#alternate implementation
#first thing. don't need to split the file into lines. just split on commas. should give us what we need
#a huge baked-in assumption is that everything will be uppercase. Need to look downstream and see if case matters. 
#The aliases have to be the same case that they came in as. The issue is 'SELECT' vs 'select' and 
#'FROM' vs 'from'
class SQL_PARSER_NEW(object):

    def __init__(self, file_name):
        self.file_name = file_name

    @property  
    def columns(self):
        return open(self.file_name, 'r').read().replace('\n','').replace('SELECT','').split(',')
