import json

def lambda_handler(event, context):
    # Retrieve the HTTP method and path from the event object
    http_method = event['httpMethod']
    path = event['path']

    if http_method == 'GET':
        if path == '/health':
            return {
                'statusCode': 200,
                'body': 'OK'
            }
        elif path == '/api':
            response_data = {
                'search': 'google',
                'output': {
                    'tlds': {
                        'com': False,
                        'org': False,
                        'net': False
                    },
                    'brand': {
                        'amazon': 3,
                        'ebay': 3,
                        'etsy': 3
                    },
                    'legal': {
                        'trademark': 3,
                        'patent': 3
                    }
                }
            }
            return {
                'statusCode': 200,
                'body': json.dumps(response_data)
            }

    # If the requested endpoint is not supported, return a 404 response
    return {
        'statusCode': 404,
        'body': 'Not Found'
    }
