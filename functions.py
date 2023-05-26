import csv
import boto3
import requests

# AWS S3 bucket information
bucket_name = 'nameo-data'
folder_with_files = 'domains/'
tld_file = 'tld/tld.csv'
location_file = 'location'

# Initialize AWS S3 client
s3 = boto3.client('s3')

def read_file_from_s3(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    return response['Body'].read().decode('utf-8')

def write_file_to_s3(bucket, key, data):
    s3.put_object(Body=data, Bucket=bucket, Key=key)

def read_location():
    try:
        location = int(read_file_from_s3(bucket_name, location_file))
    except:
        location = 0
    return location

def write_location(location):
    write_file_to_s3(bucket_name, location_file, str(location))

def combine_domains_tlds():
    # Read the TLD file
    tld_data = read_file_from_s3(bucket_name, tld_file)
    tlds = list(csv.reader(tld_data.splitlines()))

    # Get the starting location
    location = read_location()

    # Read the domain files
    domain_files = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_with_files)['Contents']
    domain_files = [obj['Key'] for obj in domain_files]

    for i in range(location, len(domain_files)):
        domain_file = domain_files[i]
        domain_data = read_file_from_s3(bucket_name, domain_file)
        domains = domain_data.split('\n')

        for domain in domains:
            for tld in tlds:
                if domain:
                    domain_tld = f"{domain}.{tld[0]}"
                    domain_checker(domain_tld, tld[1])

        location = i + 1
        write_location(location)




def domain_checker(domain, rdap_url=None):
    tld = domain.split('.')[-1]

    # Perform name server check
    # Replace this with your own name server check logic
    ns_check_result = perform_name_server_check(domain)

    # Perform WHOIS lookup
    # Replace this with your own WHOIS lookup logic
    whois_result = perform_whois_lookup(domain)

    # Perform RDAP request
    if rdap_url is None or not rdap_url.startswith("http"):
        rdap_url = f"https://root.rdap.org/domain/{tld}"
    rdap_result = perform_rdap_request(domain, rdap_url)

    # Determine if the domain is registered based on the results
    is_registered = ns_check_result or whois_result or rdap_result

    # Pass the response to the recorder function
    recorder(domain, is_registered)


def perform_name_server_check(domain):
    # Replace this with your name server check logic
    # Return True or False based on the check result
    return False


def perform_whois_lookup(domain):
    # Replace this with your WHOIS lookup logic
    # Return True or False based on the lookup result
    return False


def perform_rdap_request(domain, rdap_url):
    try:
        response = requests.get(rdap_url)
        # Replace this with your RDAP request parsing logic
        # Return True or False based on the RDAP response
        return True
    except requests.exceptions.RequestException:
        return False


def recorder(domain, is_registered):
    # Replace this with your recording logic
    # Print or save the domain and is_registered value
    print(f"Domain: {domain}, Is Registered: {is_registered}")
