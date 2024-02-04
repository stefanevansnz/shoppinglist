import json

from botocore.vendored import requests
import base64
import boto3

# Get the boto3 clients
s3 = boto3.resource('s3')
textract_client = boto3.client('textract')

bucket_name = 'stefan-sam-app-imagebuck-915922766016'
#where the file will be uploaded, if you want to upload the file to folder use 'Folder Name/FileName.jpeg'
file_name_with_extention = 'photo.png'
url_to_download = 'body.data'

#make sure there is no data:image/jpeg;base64 in the string that returns
def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    #print(json.dumps(event))
    
    #image_base64 = get_as_base64(url_to_download)
    #body = event['body']
    body = json.loads(event['body'])
    
    image_base64 = body['data']
    print("upload to s3")
    
    obj = s3.Object(bucket_name,file_name_with_extention)
    
    image_base64 = image_base64[image_base64.find(",")+1:]
    
    # print(image_base64)
    obj.put(Body=base64.b64decode(image_base64)) 
    
    #obj.put(Body=image_base64)
    
    # extract text and return
    image = {
        'S3Object':
            {
             'Bucket':  bucket_name,
             'Name': file_name_with_extention
            }
    }
    # Analyze the document.
    print("extract text")
    response = textract_client.detect_document_text(Document=image)

    # Get the lines from blocks
    lines = []
    blocks = response['Blocks']
    for block in blocks:
        if (block['BlockType'] == 'LINE'):
            line = { 'id': block['Id'], 'text': block['Text'], 'confidence': round(block['Confidence']) }
            lines.append(line)

    response = json.dumps(lines)

    #return {}
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': response
    }