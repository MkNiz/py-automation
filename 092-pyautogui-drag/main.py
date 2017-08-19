import pyautogui

pyautogui.moveTo(378, 142, duration=1.2)

# Drag left to right with relative drag
pyautogui.dragRel(260, 0, duration=2.2)
pyautogui.click()

# Drag right to left specifying coordinates
pyautogui.dragTo(378, 142, duration=1.8)
pyautogui.click()