import subprocess

print("Opening Preview...")
prev = subprocess.Popen(["open", "/Applications/Preview.app"])

prev.wait()
print("Preview executed.")