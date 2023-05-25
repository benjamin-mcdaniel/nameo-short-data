def collect_domain_data(domain):
    functions = [function1, function2, function3, function4, function5]

    for func in functions:
        result = func(domain)
        if not result:
            write_data(False, domain)
            return

    write_data(True, domain)

def function1(domain):
    # Logic for function 1
    return True

def function2(domain):
    # Logic for function 2
    return True

def function3(domain):
    # Logic for function 3
    return True

def function4(domain):
    # Logic for function 4
    return True

def function5(domain):
    # Logic for function 5
    return True

def write_data(success, domain):
    if success:
        # Logic for writing data when all functions succeed
        print(f"Writing data for successful domain: {domain}")
    else:
        # Logic for writing data when any function fails
        print(f"Writing data for failed domain: {domain}")

# Example usage
domain_to_process = "example.com"
collect_domain_data(domain_to_process)

