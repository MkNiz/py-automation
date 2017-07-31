import os

cwd = os.getcwd()

file1_path = os.path.join(cwd, "documents", "file1.txt")
file2_path = os.path.join(cwd, "documents", "file2.txt")

# Reading the whole document
file1 = open(file1_path)

file1_contents = file1.read()
print(file1_contents)

# Reading line by line
file2 = open(file2_path)

file2_contents = file2.readlines()
for idx, line in enumerate(file2_contents):
    print("LINE", idx+1, ":\t", line)