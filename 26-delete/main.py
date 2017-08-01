import os, shutil

initial_cwd = os.getcwd()
good_dir_path = os.path.join(initial_cwd, "good_dir")
bad_dir_path = os.path.join(initial_cwd, "bad_dir")

# Remove all .bad files in good_dir
for file in os.listdir(good_dir_path):
    if file.endswith('.bad'):
        print("Removing:", file)
        file_path = os.path.join(good_dir_path, file)
        os.unlink(file_path)
        
# Remove the bad directory
shutil.rmtree(bad_dir_path)
print("Removed directory:", bad_dir_path)