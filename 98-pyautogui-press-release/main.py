import pyautogui

pyautogui.moveTo(380, 250, duration=0.5)
pyautogui.click()

pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')