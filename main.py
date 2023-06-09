import json
from flask import Flask, jsonify

from functions import domain_check, amazon_check, trademark_check

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def main():
    domains = domain_check()
    amazon = amazon_check()
    trademark = trademark_check()

    output_array = [domains, amazon, trademark]
    formatted_output = [output_array[0], output_array[1], output_array[2]]
    json_data = jsonify(formatted_output)
    print (json_data)
    return json_data

if __name__ == "__main__":
    app.run()
