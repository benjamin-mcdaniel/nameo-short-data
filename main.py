import json
from flask import Flask, jsonify

from functions import domain_check, amazon_check, trademark_check
import json


prompt = "example"
extensions = ['com', 'net', 'org']

def main():
    domains = domain_check(prompt, extensions)
    amazon = amazon_check()
    trademark = trademark_check()

    output_array = {
        "domains": domains,
        "amazon": amazon,
        "trademark": trademark
    }

    json_data = json.dumps(output_array, indent=4)
    return json_data

if __name__ == "__main__":
    result = main()
    print(result)