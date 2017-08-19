import pyautogui

scr = pyautogui.screenshot()

# Get pixel value of an arbitrary position on the screen
pixRGBA = scr.getpixel((128, 128))

# Check whether it matches the same position on the screen
theyre_the_same_color = pyautogui.pixelMatchesColor(128, 128, pixRGBA)

if theyre_the_same_color:
    print("Colors match")
else:
    print("Colors don't match")