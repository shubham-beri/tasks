import boto3
dynamodb = boto3.resource('dynamodb')
def createTable(table_name):
    conn = boto3.resource('dynamodb', region_name='us-east-2')
    table1 = conn.create_table(
    TableName=table_name,
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

    table1.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    assert table1.table_status == 'ACTIVE'

    return table1


def addRow(emp_id, full_Name, age, table_name):
    conn = boto3.resource('dynamodb', region_name='us-east-2')
    table1 = conn.Table(table_name)
    return table1.put_item(
        Item={
            'emp_id': emp_id,
            'full_name': full_Name,
            'age': age
        }
    )

def retrieveRow(emp_id, table_name):
    conn = boto3.resource('dynamodb', region_name='us-east-2')
    table1 = conn.Table(table_name)
    response = table1.get_item(
        Key= {
            'emp_id': emp_id,
        }
    )

    return (response['Item'])


def updateAge(emp_id, newAge, table_name):
     conn = boto3.resource('dynamodb', region_name='us-east-2')
     table1 = conn.Table(table_name)
     return table1.update_item(
            Key={
                'emp_id': emp_id,
            },
            UpdateExpression='SET age = :val1',
            ExpressionAttributeValues={
                ':val1': newAge
            }
        )

def deleteRow(emp_id, table_name):
    conn = boto3.resource('dynamodb', region_name='us-east-2')
    return conn.Table(table_name).delete_item(
            Key={
                'emp_id': emp_id,
            }
        )
"""
conn = boto3.resource('dynamodb', region_name='us-east-2')

print(retrieveRow(conn, 'E105', 'employees'))"""
