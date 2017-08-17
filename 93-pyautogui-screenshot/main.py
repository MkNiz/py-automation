import pyautogui
from PIL import Image

scr_shot = pyautogui.screenshot()

# The return value is an image object and can be manipulated as such
scr_shot.resize((320, 240)).transpose(Image.FLIP_TOP_BOTTOM).save("screen_320_240_flip.png")
print("Screenshot saved")