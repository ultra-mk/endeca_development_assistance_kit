import os
import utils
import datatype_dictionary as dd
import re


class SQL_PARSER(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def find_index(self, sql_lines, search_item):
        for index, line in enumerate(sql_lines):
            if search_item in line:
                return index

    def remove_subq(self, sql_lines):
        return [re.sub(".*[\)]","",s) for s in sql_lines]

    @property  
    def columns(self):
        text = open(self.file_name, 'r').read().upper()
        columns = text.replace('\n','').replace('SELECT','').split(',')
        columns = self.remove_subq(columns)
        columns = columns[0:self.find_index(columns, 'FROM') + 1]
        columns[-1] = columns[-1][0:columns[-1].find('FROM')]
        return [i[i.index(' AS ') + 4:] if ' AS ' in i else i[i.index('.') + 1:] for i in columns]

    @property 
    def columns_datatypes(self):
        return [[c, dd.COLUMNS_TO_ENDECA[c] if c in dd.COLUMNS_TO_ENDECA else 'mdex:string'] for c in self.columns]
