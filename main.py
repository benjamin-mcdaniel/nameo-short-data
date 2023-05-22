from functions import *


def main():
    names_file = 'names'  # Path to the names file
    tlds_file = 'tlds'    # Path to the TLDs file
    
    domain_names = generate_domain_names(names_file, tlds_file)
    
    results = []
    
    # Check availability for each domain name
    for domain in domain_names:
        is_registered = is_domain_registered(domain)
        results.append((domain, is_registered))
    
    # Save results to a CSV file with the current date in the filename
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f'{date}_domains.csv'
    
    with open(filename, 'w') as file:
        file.write('Domain,Status\n')  # Header row
        
        for result in results:
            domain, is_registered = result
            status = 'Registered' if is_registered else 'Not Registered'
            file.write(f'{domain},{status}\n')
    
    print(f"Results saved to {filename}.")

if __name__ == '__main__':
    main()