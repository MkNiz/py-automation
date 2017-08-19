import os, shutil

cwd = os.getcwd()

source_dir_path = os.path.join(cwd, "file_source")
source_path = os.path.join(source_dir_path, "move_me.plz")
dest_dir_path = os.path.join(cwd, "file_destination")

# Rename file
renamed_path = os.path.join(source_dir_path, "renamed.txt")
shutil.move(source_path, renamed_path)
print("File renamed")

# Copy file
copied_path = os.path.join(source_dir_path, "copy.txt")
shutil.copy(renamed_path, copied_path)
print("File copied to be moved")

# Move original file without renaming
shutil.move(renamed_path, dest_dir_path)
print("File moved without renaming")

# Move copied file and rename
renamed_copy_path = os.path.join(dest_dir_path, "renamed_copy.txt")
shutil.move(copied_path, renamed_copy_path)
print("File moved and renamed")