import boto3

class table:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table1 = self.dynamodb.Table('employees')

    def createTable(self):
        self.table1 = self.dynamodb.create_table(
        TableName='employees',
        KeySchema=[
            {
                'AttributeName': 'emp_id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions= [{
          'AttributeName': 'emp_id',
        'AttributeType': 'S'
        }],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

        self.table1.meta.client.get_waiter('table_exists').wait(TableName='employees')

    def addRow(self, emp_id, full_Name, age):
        self.table1 = self.dynamodb.Table('employees')
        self.table1.put_item(
            Item={
                'emp_id': emp_id,
                'full_name': full_Name,
                'age': age
            }
        )

    def retrieveRow(self, emp_id):
        self.table1 = self.dynamodb.Table('employees')
        response = self.table1.get_item(
            Key= {
                'emp_id': emp_id,
            }
        )

        return response['Item']


    def updateAge(self, emp_id, newAge):
         self.table1 = self.dynamodb.Table('employees')
         self.table1.update_item(
                Key={
                    'emp_id': emp_id,
                },
                UpdateExpression='SET age = :val1',
                ExpressionAttributeValues={
                    ':val1': newAge
                }
            )

    def deleteRow(self, emp_id):

        self.table1.delete_item(
                Key={
                    'emp_id': emp_id,
                }
            )








t1 = table()
"""t1.createTable()
t1.addRow('E101', 'Shubham Bery', 23)
t1.addRow('E102', 'Rachel Green', 49)
t1.addRow('E103', 'Leslie Knope', 51)
t1.addRow('E104', 'Tom Haverford', 36)
t1.addRow('E105', 'Ann Perkins', 38)

print(t1.retrieveRow('E103'))
print(t1.retrieveRow('E102'))
print(t1.retrieveRow('E101'))
print(t1.retrieveRow('E105'))
print(t1.retrieveRow('E104'))
"""


print(t1.retrieveRow('E103'))
t1.updateAge('E103', 52)
print('*******************')
print(t1.retrieveRow('E103'))
t1.deleteRow('E102')

print('*******************')
#print(t1.retrieveRow('E102'))
