file = open("sample.log", "r")
for line in file:
    print(line)
    if "brandon" in line:
        print("Does this file contain something supicious?")