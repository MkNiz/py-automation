import pyautogui

find_apple = pyautogui.locateOnScreen("find_apple.png")
print("Apple location: " + str(find_apple))

pyautogui.moveTo(find_apple[0] + 4, find_apple[1] + 6, duration=1.5)
pyautogui.click()
