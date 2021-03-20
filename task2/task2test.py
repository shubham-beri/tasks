import boto3
from moto import mock_dynamodb2
import task2

@mock_dynamodb2
def test_task2():
    conn = boto3.resource('dynamodb', region_name='us-east-2')
    task2.createTable(conn, 'test12')
    res = task2.addRow(conn, 'E234', 'Rammanohar Joshi', 54, 'test12')
    try:
        assert 200 == res['ResponseMetadata']['HTTPStatusCode']
        print('Test for addRow Success!')
    except:
        print('Test Case For method addRow() Failed.')

    retrieve = task2.retrieveRow(conn,'E234','test12')
    expectedResult = {'emp_id': 'E234', 'full_name': 'Rammanohar Joshi', 'age': 54}
    try:
        assert retrieve == expectedResult
        print('Test for retrieveRow Success!')
    except:
        print('Test Case For Method retrieveRow Failed')

    update = task2.updateAge(conn,'E234', 78, 'test12')
    retrieveUpdated = task2.retrieveRow(conn,'E234','test12')

    expectedResult2 = {'emp_id': 'E234', 'full_name': 'Rammanohar Joshi', 'age': 78}
    try:
        assert retrieveUpdated == expectedResult2
        print('Test for updateAge Success!')
    except:
        print('Test Case For Method updateAge Failed')


    delete = task2.deleteRow(conn,'E234', 'test12')
    try:
        deletedRetrieve = task2.retrieveRow(conn,'E234','test12')
    except:
        print('Test Success')




test_task2()

