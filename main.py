my_file = open("requiredCS.txt", "r")
all_lines = my_file.readlines()
for line in all_lines:
    upper_case_line = line.upper()
    upper_case_line = upper_case_line.strip()
    print(upper_case_line)
print("Those are the required COMP courses for the major")