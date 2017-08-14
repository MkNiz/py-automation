import subprocess, os

image_path = os.path.join(os.getcwd(), "kitty.jpg")

print("Opening Preview...")
prev = subprocess.Popen(["open", "/Applications/Preview.app", image_path])

prev.wait()
print("Preview executed.")