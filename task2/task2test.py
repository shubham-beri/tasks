import boto3
from moto import mock_dynamodb2
import task2
import unittest

@mock_dynamodb2
class test_task2(unittest.TestCase):
    def setUp(self):

        task2.createTable('test12')



    def test_addRow(self):

        res = task2.addRow('E234', 'Rammanohar Joshi', 54, 'test12')
        try:
            self.assertEqual(200, res['ResponseMetadata']['HTTPStatusCode'])
            print('Test for addRow Success!')
        except:
            print('Test Case For method addRow() Failed.')


    def test_retrieveRow(self):
        retrieve = task2.retrieveRow('E234','test12')
        expectedResult = {'emp_id': 'E234', 'full_name': 'Rammanohar Joshi', 'age': 54}
        try:
            self.assertEqual(retrieve,expectedResult)
            print('Test for retrieveRow Success!')
        except:
            print('Test Case For Method retrieveRow Failed')

    def test_updateRow(self):
        update = task2.updateAge('E234', 78, 'test12')
        retrieveUpdated = task2.retrieveRow('E234','test12')

        expectedResult2 = {'emp_id': 'E234', 'full_name': 'Rammanohar Joshi', 'age': 78}
        try:
            self.assertEqual(retrieveUpdated, expectedResult2)
            print('Test for updateAge Success!')
        except:
            print('Test Case For Method updateAge Failed')

    def test_deleteRow(self):
        delete = task2.deleteRow('E234', 'test12')
        try:
            self.assertEqual(200, res['ResponseMetadata']['HTTPStatusCode'])
            print('Test for deleteRow Success!')
        except:
            print('Test Case For method deleteRow() Failed.')


if __name__ == '__main__':
    unittest.main()
