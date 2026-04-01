file = open("sample.log", "r") # Open the log file for reading
count = 0 # Counter for lines containing "ERROR"
failed_ips = {} # Dictionary to store failed IP addresses and their counts
 
for line in file:
    if "ERROR" in line:
        print(line)
        print("This file contains an error message.")
        count += 1

    if "Failed" in line:
        ip = line.split("from ")[-1].strip()
        if ip in failed_ips:
            failed_ips[ip] += 1
        else:
            failed_ips[ip] = 1

    for ip, attempts in failed_ips.items():
        print(f"IP: {ip}, Failed attempts: {attempts}")

        for ip, attempts in failed_ips.items():
            if attempts > 3:
                print(f"IP: {ip} has {attempts} failed attempts. Consider blocking this IP.")

print(f"Total error lines: {count}")
 
