import json

def lambda_handler(event, context):
    print(event)
    print(type(event['body']))
    print(event['body'])
    body_json = json.loads(event['body'])
    a = body_json['a']
    b = body_json['b']
    response = str(a + b)
    print(response)
    return {
        'statusCode': 200,
        'body': response
    }
