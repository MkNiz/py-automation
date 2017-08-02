import os, zipfile, shutil

cwd = os.getcwd()

print("- [ Extension Collector ] -")
ext = ''

while((len(ext) > 4 or len(ext) < 1) or ('.' in ext)):
    ext = input("Please input an extension (1-4 characters, no dot):\n~> ")
print('')

if not os.path.exists(ext):
    os.makedirs(ext)
    
dest_dir = os.path.join(cwd, ext)
    
dotext = '.' + ext

print("__________\n")
for dir, _, files in os.walk(cwd):
    if dir != dest_dir:
        print("Checking directory:")
        print(dir, "\n")
        for f in files:
            if f.endswith(dotext):
                print("Found:", f, "\n")
                f_path = os.path.join(dir, f)
                shutil.copy(f_path, dest_dir)
            elif f.endswith(".zip"):
                z_path = os.path.join(dir, f)
                z = zipfile.ZipFile(z_path)
                for item in z.namelist():
                    if item.endswith(dotext):
                        print("In Archive:", z_path)
                        print("Found:", item, "\n")
                        z.extract(item, dest_dir)
        print("__________\n")

shutil.make_archive(ext, 'zip', dest_dir)

print("Zip file '" + ext + ".zip' created.\n")
    

            
            
        