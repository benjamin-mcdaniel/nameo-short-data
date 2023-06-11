import requests
import xml.etree.ElementTree as ET

url = "https://assignment-api.uspto.gov/trademark/lookup"
params = {
    "query": "coke",
    "filter": "*"
}
headers = {
    "Accept": "application/xml"
}

try:
    response = requests.get(url, params=params, headers=headers, verify=False)
    if response.status_code == 200:
        # Parse the XML response
        xml_data = response.text
        root = ET.fromstring(xml_data)

        # Process the trademark data
        trademark_data = root.find("result")
        if trademark_data is not None:
            for item in trademark_data:
                # Access individual data elements as needed
                mark_desc = item.find("markDesc").text
                registrant = item.find("registrant").text
                filing_date = item.find("filingDate").text

                # Perform further processing or output the data
                print("Trademark: {}".format(mark_desc))
                print("Registrant: {}".format(registrant))
                print("Filing Date: {}".format(filing_date))
                print("----------------------")
        else:
            print("No trademark data found.")
    else:
        print("Error:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error:", e)
