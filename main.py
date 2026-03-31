file = open("sample.log", "r")
count = 0
failed_ips = {}
 # ERROR detection
for line in file:
    if "ERROR" in line:
        print(line)
        print("This file contains an error message.")
        count += 1

print(f"Total error lines: {count}")

  # FAILED login detection