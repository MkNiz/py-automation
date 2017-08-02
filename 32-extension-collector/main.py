import os, shutil
import collector

cwd = os.getcwd()

ignore_dirs = ["__pycache__", "__MACOSX"]

print("- [ Extension Collector ] -")
ext = collector.get_ext()
dotext = '.' + ext

ignore_dirs.append(ext)

if not os.path.exists(ext):
    os.makedirs(ext)
    
dest_dir = os.path.join(cwd, ext)

print("__________\n")
for dir, subdirs, files in os.walk(cwd):
    subdirs[:] = [d for d in subdirs if d not in ignore_dirs]
    collector.check_dir(dir, dest_dir, files, dotext)

shutil.make_archive(ext, 'zip', dest_dir)

print("Zip file '" + ext + ".zip' created.\n")

            
            
        