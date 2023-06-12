import json
import configparser
import sys
import os

# Get the path to the INI file from command-line arguments
ini_file = sys.argv[1]

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

    # Convert the extensions string to a list
    extensions = extensions_str.split(',')

from source.brand import *
from source.domain import *
from source.legal import *

def main():
    domains = domain_main(prompt, extensions)
    trademark = trademark_main(prompt)
    patent = patent_main(prompt)
    brand = brand_main(prompt)



    output_array = {
        "domains": domains,
        "brand": brand,
        "patent": patent,
        "trademark": trademark
    }

    json_data = json.dumps(output_array, indent=4)
    return json_data

if __name__ == "__main__":
    result = main()
    print(result)
