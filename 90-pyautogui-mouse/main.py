import pyautogui

# Get current screen size
screenW, screenH = pyautogui.size()

# Move the cursor around the edge of the screen
pyautogui.moveTo(64, 64)
pyautogui.moveTo(screenW - 64, 64, duration=1.0)
pyautogui.moveTo(screenW - 64, screenH - 64, duration=0.75)
pyautogui.moveTo(64, screenH - 64, duration=1.0)
pyautogui.moveTo(64, 64, duration=0.75)

# Move the cursor relative to its current position
for _ in range(4):
    pyautogui.moveRel(64, 64, duration=0.5)
    pyautogui.moveRel(64, -64, duration=0.5)
    
# Get and print mouse position
xPos, yPos = pyautogui.position()
print("Mouse ended at position: ({0}, {1}).".format(xPos, yPos))