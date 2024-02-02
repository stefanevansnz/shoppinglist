import json
def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))
    response = {}

    #return {}
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps('Image uploaded')
    }