import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('martialarts')

response = table.delete_item(Key = {'style': 'Karate', 'location': 'Japan'})

print(response)