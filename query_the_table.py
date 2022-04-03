#import boto3
import boto3
#this code will allow us to set the conditions of our scan or query
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('martialarts')
#here we set what we are looking for
response = table.query(
    KeyConditionExpression=Key('style').eq('Karate')
)
#this piece of code here wll prit the results    
items = response['Items']
print(items)
