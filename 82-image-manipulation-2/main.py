from PIL import Image

my_img = Image.new('RGBA', (320, 240), (200, 200, 200, 255))

my_img.save('light-blank.png')
print("Saved image")