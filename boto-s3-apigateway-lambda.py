# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# S3 Access

# import boto3


# s3 = boto3.resource('s3')


# for bucket in s3.buckets.all():
#     print(bucket.name)
    
# # Upload a new file
# #data = open('C:\\Users\\harishs\\Pictures\\anime.png', 'rb')
# #s3.Bucket('mytestbucketsiva').put_object(Key='anime.png', Body=data)

# obj = s3.Object("mytestbucketsiva", "anime.png")
# obj.delete()


# # API Gateway with Lambda

# import json

# print('Loading function')

# def lambda_handler(event, context):
#     #1. Parse out query string params
#     transactionId = event['queryStringParameters']['transactionId']
#     transactionType = event['queryStringParameters']['type']
#     transactionAmount = event['queryStringParameters']['amount']

#     print('transactionId=' + transactionId)
#     print('transactionType=' + transactionType)
#     print('transactionAmount=' + transactionAmount)

#     #2. Construct the body of the response object
#     transactionResponse = {}
#     transactionResponse['transactionId'] = transactionId
#     transactionResponse['type'] = transactionType
#     transactionResponse['amount'] = transactionAmount
#     transactionResponse['message'] = 'Hello from Lambda land'

#     #3. Construct http response object
#     responseObject = {}
#     responseObject['statusCode'] = 200
#     responseObject['headers'] = {}
#     responseObject['headers']['Content-Type'] = 'application/json'
#     responseObject['body'] = json.dumps(transactionResponse)

#     #4. Return the response object
#     return responseObject

#https://5uwwajl0j7.execute-api.us-east-1.amazonaws.com/test/transactions?transactionId=2&type=purchase&amount=100

#https://5uwwajl0j7.execute-api.us-east-1.amazonaws.com/test/transactions?num1=5&num2=4

#: https://5uwwajl0j7.execute-api.us-east-1.amazonaws.com/test1?num1=5&num2=4

https://v2rqjkg61k.execute-api.us-east-1.amazonaws.com/test/add?num1=5&num2=4

import json

print('Loading function')

def lambda_handler(event, context):
    
    #1. Parse out query string params
    num1 = event['queryStringParameters']['num1']
    num2 = event['queryStringParameters']['num2']
    
    print('number1=' + num1)
    print('number2=' + num2)    
    sum = int(num1) + int(num2)
            
    #2. Construct the body of the response object
    response = {}
    response['Sum'] = sum
    response['num1'] = num1
    response['num2'] = num2
    response['message'] = 'Hello from Lambda land'

    #3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = event["headers"]
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)

    #4. Return the response object
    return responseObject