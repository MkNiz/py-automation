import os

path_rel = os.path.join('.', 'jams')

# Return the absolute path corresponding to a relative path
path_abs = os.path.abspath(path_rel)
print("Absolute path corresponding to './jams' (or '.\\jams'):")
print(path_abs, "\n")

# Check if a path is absolute
print("Is the initial path absolute?", os.path.isabs(path_rel))
print("Is the modified path absolute?", os.path.isabs(path_abs), "\n")

# Create a relative path from a startpoint (default CWD) to the absolute path provided
print("Relative path from working directory to the absolute path:")
print(os.path.relpath(path_abs), "\n")

# Get the 'dirname' of a path, or everything before the last slash
print("Path dirname:")
print(os.path.dirname(path_abs), "\n")

# Get the 'base name' of a path, or everything after the last slash
print("Path base name:")
print(os.path.basename(path_abs), "\n")

# Get a tuple value of the separated dirname and base name of a path
path_tuple = os.path.split(path_abs)
print("Dirname from tuple:", path_tuple[0])
print("Base name from tuple:", path_tuple[1], "\n")

# Using a string's split function combined with os.path.sep
# can create a list of all the paths up to the destination
path_list = path_abs.split(os.path.sep)
print("Directories:")
for dir in path_list:
    print("\t", dir)
