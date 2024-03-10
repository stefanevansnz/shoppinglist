import json
import boto3

# Initialize the AWS Bedrock client
bedrock = boto3.client(service_name="bedrock", region_name="us-east-1")

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))
    inputBody = json.loads(event.body)
    print(inputBody)    
    inputValue = inputBody['data']['input']
    print(inputValue)
    prompt = f"\n\nHuman:Generate a step by step recipe for " + inputValue + ".\n\nAssistant:"

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 300
    })

    modelId = "anthropic.claude-instant-v1"
    accept = 'application/json'
    contentType = 'application/json'


    # Initialize the AWS Bedrock client
    bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-west-2")
    
    response = bedrock.invoke_model_with_response_stream(
        modelId=modelId,
        body=body
    )
    
    generated_recipe = ""
    if response and 'body' in response:
        stream = response.get('body')
        if stream:
            for event in stream:
                chunk = event.get('chunk')
                if chunk:
                    chunk_text = json.loads(chunk.get('bytes').decode())
                    completion = chunk_text.get('completion', '')
                    if completion:
                        generated_recipe += completion

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': generated_recipe
    }