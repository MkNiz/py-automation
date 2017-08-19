import shutil, os

cwd = os.getcwd()

# Copy a file
file_path = os.path.join(cwd, "files", "a_file.txt")
destination_path = os.path.join(cwd, "files", "a_file_copy.txt")

shutil.copy(file_path, destination_path)
print("File copied.")

# Copy a directory
directory_path = os.path.join(cwd, "files")
destination_path = os.path.join(cwd, "files_copy")

shutil.copytree(directory_path, destination_path)
print("Directory copied.")