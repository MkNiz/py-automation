import os

myCWD = os.getcwd()
print("Current Working Directory:")
print(myCWD, "\n")

path1 = os.path.join(myCWD, "butts.exe")
print("A fake file in the current working directory:")
print(path1, "\n")

path2 = os.path.join(myCWD, "jokes", "good jokes")
print("A fake directory based in the current working directory:")
print(path2, "\n")

new_cwd = os.path.join(myCWD, "deep-dir-pizza")
os.chdir(new_cwd)
myCWD = os.getcwd()
print("New Working Directory:")
print(myCWD, "\n")

path3 = os.path.join(myCWD, "hello.txt")
print("An existing file in the new current working directory:")
print(path3)