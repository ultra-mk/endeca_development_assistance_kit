import unittest
from edak import __main__ as m


class MAIN_TEST(unittest.TestCase):

    def test_check_for_file_false(self):
        self.assertEqual(False, m.check_for_file('this_file_doesnt_exist.txt'))

    def test_check_for_file_true(self):
        self.assertEqual(True, m.check_for_file('endeca_attributes.xlsx'))


if __name__ == '__main__':
    unittest.main()
