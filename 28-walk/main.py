import os

cwd = os.getcwd()

for currentDir, subDirs, dirFiles in os.walk(cwd):
    print("At:", currentDir)
    print("Child Directories:")
    for subDir in subDirs:
        print("\t" + subDir)
    print("Files:")
    for f in dirFiles:
        print("\t" + f)
    print('__________')