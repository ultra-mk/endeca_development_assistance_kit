import sys
import os
import time
import reader_writer as rw
import sql_generator
import eql_generator
import xml_generator
import utils


def main(args=None):
    validate_input_and_run()


def validate_input_and_run():
    file_name = get_filename_from_user()
    if utils.check_for_file(file_name):
        file_type = get_format_option_from_user()
        run_reader_writer_functions(file_name, file_type)
    else:
        print 'file not found'
        time.sleep(1)
        quit = raw_input('type quit to quit: ')
        if quit == 'quit':
            sys.exit
        else:
            validate_input_and_run()


def get_filename_from_user():
    return raw_input("What is the name of your attribute file?: ")


def get_format_option_from_user():
    print "Which file formats do you need?"
    print "Select 1 for PLSQL"
    print "Select 2 for EQL"
    print "Select 3 for XML"
    print "Select 4 for all formats."
    return raw_input("Please make your selection. ")


def run_reader_writer_functions(file_name, file_type):
    if file_type == '1':
        sql_reader_writer(rw.Excel_Reader(file_name),
                          rw.Text_Writer('sql.txt'))
    elif file_type == '2':
        eql_reader_writer(rw.Excel_Reader(file_name),
                          rw.Text_Writer('eql.txt'))
    elif file_type == '3':
        xml_reader_writer(rw.Excel_Reader(file_name),
                          rw.Text_Writer('xml.txt'))
    elif file_type == '4':
        sql_reader_writer(rw.Excel_Reader(file_name),
                          rw.Text_Writer('sql.txt'))
        eql_reader_writer(rw.Excel_Reader(file_name),
                          rw.Text_Writer('eql.txt'))
        xml_reader_writer(rw.Excel_Reader(file_name),
                          rw.Text_Writer('xml.txt'))
    else:
        print 'please enter a correct option'


def sql_reader_writer(reader, writer):
    print 'writing some sweet PLSQL for you........'
    writer.clear_file()
    for r in reader.attribute_data:
        sql = sql_generator.SQL(*r)
        writer.save_text(sql.generate_sql())
    print 'beep, boop your PLSQL is ready!'


def eql_reader_writer(reader, writer):
    print 'writing some sweet EQL for you...........'
    writer.clear_file()
    writer.save_text(eql_generator.EQL(reader.eql_attributes, 'view1').generate_eql())
    print 'beep, boop, your EQL is ready!'


def xml_reader_writer(reader, writer):
    xml_instance = xml_generator.XML(reader.xml_attributes, 'metadata1')
    if xml_instance.validate_data_types():
        print 'writing some sweet XML for you'
        writer.clear_file()
        writer.save_text(xml_instance.generate_xml())
        print 'beep, boop your XML is ready'
    else:
        print 'it seems you have an issue with your datatypes in your spreadsheet.'
        print 'please double check for spelling errors and try again'
        time.sleep(1)
        validate_input_and_run()


if __name__ == '__main__':
    main()
