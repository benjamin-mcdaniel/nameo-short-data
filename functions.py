import whois
import datetime

def is_domain_registered(domain):
    try:
        whois.whois(domain)
        return True  # Domain is registered
    except whois.parser.PywhoisError:
        return False  # Domain is not registered

def generate_domain_names(names_file, tlds_file):
    domain_names = []
    
    # Read names from the names file
    with open(names_file, 'r') as file:
        names = file.read().splitlines()
    
    # Read TLDs from the TLD file
    with open(tlds_file, 'r') as file:
        tlds = file.read().splitlines()
    
    # Generate domain names by combining names and TLDs
    for name in names:
        for tld in tlds:
            domain_names.append(name + '.' + tld)
    
    return domain_names

