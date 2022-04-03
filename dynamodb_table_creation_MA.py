# first we must import boto3 
import boto3
# now we are calling the dynamodb command. make sure your region is correct
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
# here we are now creating the table
table = dynamodb.create_table(
    TableName='Martial Arts',
    KeySchema=[
        {
            'AttributeName': 'style',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'location',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'style',
            'AttributeType': 'S' #'s' means string
        },
        {
            'AttributeName': 'location',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)

