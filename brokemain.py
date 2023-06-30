import json
import configparser
import sys
import os
import socket


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


def brand_main(prompt, marketplaces):
    market_results = {}
    for market in marketplaces:
        # Perform an actual search in the marketplaces
        # Replace the placeholder value with the appropriate search logic
        market_search = 3
        market_results[market] = market_search

    return market_results


def health_main():
    domain_health_check()
    brand_health_check()
    print("health checks passed")


def domain_health_check():
    # Assume the health check checks the availability of Google's domain
    google_domain = "google.com"

    # Perform the health check
    if is_domain_available(google_domain):
        print("Google domain is available.")
    else:
        error_message = "health google domain failed"
        raise SystemExit(error_message)


def is_domain_available(domain):
    # Perform a real domain availability check
    try:
        socket.gethostbyname(domain)
        return False  # Domain is registered
    except socket.error:
        return True  # Domain is not registered


def brand_health_check():
    # Assume the health check checks the presence of Google as a brand
    google_brand = "Google"

    # Perform the health check
    if is_brand_present(google_brand):
        print("Google brand is present.")
    else:
        error_message = "health google brand failed"
        raise SystemExit(error_message)


def is_brand_present(brand):
    # Add your brand presence check logic here
    # For demonstration purposes, always assume the brand is present
    return True


def trademark_main(prompt):
    trademark = prompt.lower()
    # Check if domain is available on trademark database
    # Replace the placeholder value with the appropriate check logic
    check = 223
    return check


def patent_main(prompt):
    patent = prompt.lower()
    # Check if domain is available on patent database
    # Replace the placeholder value with the appropriate check logic
    check = 32
    return check


def domain_main(prompt, extensions):
    available_domains = {}
    for extension in extensions:
        full_domain = f"{prompt}.{extension}"
        is_registered = domain_lookup(full_domain)
        available_domains[extension] = is_registered
    return available_domains


def domain_lookup(domain):
    try:
        socket.gethostbyname(domain)
        return False  # Domain is registered
    except socket.error:
        return True  # Domain is not registered


# Check if the script is running as a Lambda function
if 'LAMBDA_TASK_ROOT' in os.environ:
    def lambda_handler(event, context):
        args = (event['arg_type'], event['arg_string'])
        result = run_code(args)
        return result
else:
    if __name__ == "__main__":
        # Run code locally with example arguments
        args = ('fuzz', 'example string')
        result = run_code(args)
        print(result)
