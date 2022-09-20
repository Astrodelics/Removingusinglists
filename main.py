my_file = open("requiredCS.txt", "r")
all_lines = my_file.readlines()
for line in all_lines:
    print(line)