import unittest
import eee_sql as e

class EEE_SQL_TEST(unittest.TestCase):

	@classmethod
	def setUpClass(EEE_SQL_TEST):
		EEE_SQL_TEST.insert_attr = e.Insert_attribute(204,'accounting_period', 'mdex:string')

	def test_init_Insert_attribute(self):
		self.assertEqual(204, EEE_SQL_TEST.insert_attr.eid_instance_id)
		self.assertEqual('accounting_period', EEE_SQL_TEST.insert_attr.eid_instance_attribute) 
		self.assertEqual('mdex:string', EEE_SQL_TEST.insert_attr.datatype)

	def test_Insert_attribute_create_sql(self):
		self.assertEqual('SET DEFINE OFF;\nCOMMIT;', EEE_SQL_TEST.insert_attr.create_sql())






if __name__ == '__main__':
	unittest.main()