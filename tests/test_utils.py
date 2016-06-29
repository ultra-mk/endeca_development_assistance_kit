import unittest
from edak import utils


class UTILS_TEST(unittest.TestCase):

    def test_check_for_file_false(self):
        self.assertFalse(utils.check_for_file('this_file_does_not_exits.py'))

    def test_check_for_file_true(self):
        self.assertTrue(utils.check_for_file('endeca_attributes.xlsx'))

    def test_open_file_split_into_lines(self):
        self.assertEqual(
            'SELECT', utils.open_file_split_into_lines('sql_parser_test_doc.sql')[0])
