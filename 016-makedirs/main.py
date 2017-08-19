import os

myCWD = os.getcwd()
myDir = os.path.join(myCWD, "japes", "jests", "foolery")

os.makedirs(myDir)
print("Created directory:")
print(myDir)