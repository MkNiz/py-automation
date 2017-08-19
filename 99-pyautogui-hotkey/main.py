import pyautogui

print("Hello")

pyautogui.moveTo(378, 140, duration=0.5)
pyautogui.dragRel(90, 0, duration=0.75)

pyautogui.hotkey('command', 'c')

pyautogui.moveTo(378, 308, duration=0.25)

pyautogui.click()
pyautogui.hotkey('command', 'v')

