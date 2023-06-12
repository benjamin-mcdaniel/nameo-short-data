
import socket


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
    
