

import socket

def amazon_check():
    # Check if domain is available on Amazon
    # Return True or False
    check = False
    return check

def trademark_check():
    # Check if domain is available on trademark database
    # Return True or False
    check = True
    return check


def domain_check(prompt, extensions):
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