import os

cwd = os.getcwd()

# Get the size of a file in bytes
readme_path = os.path.join(cwd, 'readme.md')
print("Size of readme.md:", os.path.getsize(readme_path), "bytes\n")

# Get a list of files in a directory
file_list = os.listdir(cwd)
print("Files in CWD:")
for f in file_list:
    print("\t", f)
print("")

real_path = os.path.join(cwd, 'real')
fake_path = os.path.join(cwd, 'fake')
real_file_path = os.path.join(cwd, 'real', 'existing_file.txt')
fake_file_path = os.path.join(cwd, 'real', 'nonexisting_file.txt')

# Check if a directory or file exists
print("Does a 'real' directory exist?", os.path.exists(real_path))
print("Does a 'fake' directory exist?", os.path.exists(fake_path))
print("Does 'real/existing_file.txt' exist?", os.path.exists(real_file_path))
print("Does 'real/nonexisting_file.txt' exist?", os.path.exists(fake_file_path))
print("")

# Check if a path is leading to a file
print("Is 'real' a file?", os.path.isfile(real_path))
print("Is 'fake' a file?", os.path.isfile(fake_path))
print("Is 'real/existing_file.txt' a file?", os.path.isfile(real_file_path))
print("Is 'real/nonexisting_file.txt' a file?", os.path.isfile(fake_file_path))
print("")

# Check if a path is leading to a directory
print("Is 'real' a directory?", os.path.isdir(real_path))
print("Is 'fake' a directory?", os.path.isdir(fake_path))
print("Is 'real/existing_file.txt' a directory?", os.path.isdir(real_file_path))
print("Is 'real/nonexisting_file.txt' a directory?", os.path.isdir(fake_file_path))
