from PIL import Image

kity = Image.open("kitty.jpg")
cropped_kity = kity.crop((0, 0, 320, 240))

cropped_kity.save("cropped_kitty.jpg")
print("Image saved")