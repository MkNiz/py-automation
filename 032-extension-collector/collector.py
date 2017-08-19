# Contains functions to aid the extension collector
import os, zipfile, shutil

def get_ext():
    """Returns a user-input extension when conditions are reached"""
    ext = ''
    while((len(ext) > 4 or len(ext) < 1) or ('.' in ext)):
        ext = input("Please input an extension (1-4 characters, no dot):\n~> ")
    print('')
    return ext

def copy_file(f, dir, dest):
    """Copies the file f within dir to the destination directory"""
    print("Found:", f, "\n")
    f_path = os.path.join(dir, f)
    shutil.copy(f_path, dest)
    
def check_zip(z_path, dir, dest, dotext):
    """Checks within a zip file for files with the extension dotext, and 
    extracts them to dest when found"""
    z = zipfile.ZipFile(z_path)
    for item in z.namelist():
        if item.endswith(dotext) and not item.startswith("__MACOSX"):
            print("In Archive:", z_path)
            print("Found:", item, "\n")
            z.extract(item, dest)
    
def check_file(f, dir, dest, dotext):
    """Checks whether the file is the given extension or a zip, and sends
    it to the corresponding function"""
    if f.endswith(dotext):
        copy_file(f, dir, dest)
    elif f.endswith(".zip"):
        z_path = os.path.join(dir, f)
        check_zip(z_path, dir, dest, dotext)
        
def check_dir(dir, dest, files, dotext):
    """Scan the directory for files to check"""
    if dir != dest:
        print("Checking directory:")
        print(dir, "\n")
        for f in files:
            check_file(f, dir, dest, dotext)
        print("__________\n")