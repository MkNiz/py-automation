import os

cwd = os.getcwd()

file1_path = os.path.join(cwd, "documents", "file1.txt")
file2_path = os.path.join(cwd, "documents", "file2.txt")

# Write mode

file1 = open(file1_path, 'w')
file1.write("This file didn't exist until the script created it.\nIt will always be overwritten.")
file1.close()

# Reading to grab line position in file2
file2 = open(file2_path)
line_pos = len(file2.readlines()) + 1
file2.close()

# Using line_pos as part of the process of appending to cgi_file2
file2 = open(file2_path, 'a')
file2.write("This was appended to line {0}.\n".format(line_pos))
file2.close()

# Reading the current state of both files
file1 = open(file1_path)
file2 = open(file2_path)

print("File 1:")
print(file1.read(), "\n")

print("File 2:")
print(file2.read())