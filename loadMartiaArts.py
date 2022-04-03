
# this s the script to load the data into the table  
import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('martialarts')

with open("martialartsdata.json") as json_file:
    MartialArts = json.load(json_file)
    for MartialArt in MartialArts:
        style = MartialArt['style']
        location = MartialArt['location']

        print("Adding martial art:", style,location)

        table.put_item(
           Item={
               'style': style,
               'location': location,
            }
        )
#this is a comment