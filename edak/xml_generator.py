import datatype_dictionary as dd


class XML(object):
    CLOSE_XML = '\n</Record>\n</Metadata>'

    def __init__(self, field_names_and_datatypes, record_name):
        self.record_name = record_name
        self.field_names_and_datatypes = field_names_and_datatypes

    def metadata_id(self, metadata_id):
        return '<Metadata id="{}" previewAttachmentCharset="ISO-8859-1">\n'.format(metadata_id)

    def record_id(self, record_name):
        return r'<Record fieldDelimiter="|" name="{}" previewAttachmentCharset="ISO-8859-1" recordDelimiter="\r\n" recordSize="-1" type="delimited">\n'.format(record_name)

    def validate_data_types(self):
        data_types = [f[1] for f in self.field_names_and_datatypes]
        return set(data_types).issubset(dd.ENDECA_TO_XML.keys())

    def single_field(self, attribute_name, datatype):
        return '<Field name="' + attribute_name + '" type="' + dd.ENDECA_TO_XML[datatype] + '"/>'

    def all_fields(self, fields_and_datatypes):
        fields = [self.single_field(f[0], f[1]) for f in fields_and_datatypes]
        return '\n'.join(fields)

    def generate_xml(self):
        return self.metadata_id(id(self)) + self.record_id(self.record_name) + self.all_fields(self.field_names_and_datatypes) + self.CLOSE_XML
