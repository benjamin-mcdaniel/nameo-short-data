
import configparser
import dns.resolver
import dns.exception

def is_domain_registered(domain):
    config_file = "config.ini"  # Path to the configuration file
    dns_servers = ["8.8.8.8", "8.8.4.4", "208.67.222.222", "208.67.220.220"]  # List of DNS servers

    # Read dns_switch_after value from the configuration file
    config = configparser.ConfigParser()
    config.read(config_file)
    dns_switch_after = int(config.get("DNS", "dns_switch_after"))

    # Retrieve the DNS server to use based on the round-robin selection
    index = 0
    if dns_switch_after > 0:
        with open("call_counter.txt", "r+") as file:
            num_calls = file.read().strip()
            if num_calls:
                num_calls = int(num_calls)
            else:
                num_calls = 0
            file.seek(0)
            file.write(str(num_calls + 1))
            file.truncate()
            index = num_calls // dns_switch_after % len(dns_servers)

    dns_server = dns_servers[index]

    # Configure DNS resolver with the selected DNS server
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]

    try:
        answers = resolver.query(domain, "NS")
        return True  # Domain has at least one nameserver configured
    except dns.resolver.NoAnswer:
        return "maybe"  # Domain might not have any nameserver configured
    except dns.exception.DNSException:
        return False  # An error occurred during DNS resolution

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

