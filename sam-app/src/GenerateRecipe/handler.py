import json
from bedrock import Bedrock

def handler(event, context):
    
    body = json.loads(event['body'])
    inputValue = body['data']
    print("GenerateRecipe Handler InputValue:")
    print(inputValue)

    bedrock = Bedrock()
    generated_recipe = bedrock.generateRecipe(inputValue)
    print(generated_recipe)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': generated_recipe
    }

# local test
event = {
    "resource": "/recipe",
    "path": "/recipe",
    "httpMethod": "POST",
    "body": "{\"data\":\"meatballs\"}",
}
response = handler(event, None)
print(response)