import json
import configparser
import sys
import os

from source.brand import brand_main
from source.domain import domain_main
from source.legal import trademark_main, patent_main
from source.health import health_main

def run_code(args):
    arg_type, arg_string = args

    # Get the path to the INI file from command-line arguments
    if len(sys.argv) > 1:
        ini_file = sys.argv[1]
    else:
        ini_file = "vars.ini"

    # Check if the CICD environment variable is set to "yes"
    cicd = os.environ.get('CICD', '').lower() == 'yes'

    # If CICD is not set or set to a value other than "yes", import variables from INI file
    if not cicd:
        # Create a configparser instance
        config = configparser.ConfigParser()

        # Read the INI file
        config.read(ini_file)

        # Retrieve variables from the 'Variables' section
        variables = config['Variables']

        # Get the values for prompt and extensions
        prompt = variables.get('prompt')
        extensions_str = variables.get('extensions')
        marketplaces_str = variables.get('marketplaces')

        # Convert the extensions string to a list
        extensions = extensions_str.split(',')
        marketplaces = marketplaces_str.split(',')

    def main():
        health_main()

        domains = domain_main(prompt, extensions)
        trademark = trademark_main(prompt)
        patent = patent_main(prompt)
        brand = brand_main(prompt, marketplaces)

        output_array = {
            "domains": domains,
            "brand": brand,
            "patent": patent,
            "trademark": trademark
        }

        response = {}

        if arg_type == 'fuzz':
            response['fuzz'] = 'yes'
        elif arg_type == 'raw':
            response['raw'] = 'yes'

        response['search'] = arg_string
        response['output'] = output_array

        json_data = json.dumps(response, indent=4)
        return json_data

    result = main()
    return result

# Check if the script is running as a Lambda function
if 'LAMBDA_TASK_ROOT' in os.environ:
    def lambda_handler(event, context):
        args = (event['arg_type'], event['arg_string'])
        result = run_code(args)
        return result
else:
    # Run code locally with example arguments
    args = ('fuzz', 'example string')
    result = run_code(args)
    print(result)
