import subprocess, sys

print("Opening Script:")
my_py = subprocess.Popen([sys.executable, "hello.py"])

my_py.wait()
print("Script executed.")