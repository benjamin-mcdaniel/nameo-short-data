import whois

def is_domain_registered(domain):
    try:
        whois.whois(domain)
        return True  # Domain is registered
    except whois.parser.PywhoisError:
        return False  # Domain is not registered
