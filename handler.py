import json
import pdfkit
import boto3
import os
import base64

client = boto3.client('s3')

# Get the bucket name environment variables to use in our code
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

def generate_pdf(event, context):
    
    # Defaults
    key = 'default-filename.pdf'
    html = "<html><head></head><body><h1>It works! This is the default PDF.</h1></body></html>"
    w = '215.9'
    h = '279.4'
    
    # TODO: Validate filename and html exist
    # TODO: Clean the filename
    # TODO: Add .pdf extension if necessary
    # TODO: Add a UUID to the key

    # Decode json and set values for our pdf    
    if 'body' in event:
        data = json.loads(event['body'])
        key = data['filename']
        base64_message = data['html']
        base64_bytes = base64_message.encode('utf-8')
        message_bytes = base64.b64decode(base64_bytes)
        html = message_bytes.decode('utf-8')
        w = data['width']
        h = data['height']


    # Set file path to save pdf on lambda first (temporary storage)
    filepath = '/tmp/{key}'.format(key=key)
    
    options = {
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0',
        'orientation': 'Portrait',
        'page-width': w,
        'page-height': h
    }
    # Create PDF
    config = pdfkit.configuration(wkhtmltopdf="binary/wkhtmltopdf")
    pdfkit.from_string(html, filepath, configuration=config, options=options)
    

    # Upload to S3 Bucket
    r = client.put_object(
        ACL='public-read',
        Body=open(filepath, 'rb'),
        ContentType='application/pdf',
        Bucket=S3_BUCKET_NAME,
        Key=key
    )
    
    # Format the PDF URI
    object_url = "https://{0}.s3.amazonaws.com/{1}".format(S3_BUCKET_NAME, key)

    # Response with result
    response = {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "statusCode": 200,
        "body": object_url
    }

    return response