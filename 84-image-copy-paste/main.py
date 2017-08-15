from PIL import Image

kity = Image.open("kitty.jpg")
cat_icon = Image.open("cat_icon.png")

# Copy kitty image
kity_copy = kity.copy()

kW, kH = kity_copy.size

# Paste icon image in corners
kity_copy.paste(cat_icon, (48, 48))
kity_copy.paste(cat_icon, (kW-48, 48))
kity_copy.paste(cat_icon, (48, kH-48))
kity_copy.paste(cat_icon, (kW-48, kH-48))

kity_copy.save("kitty_bordered.jpg")
print("Image saved")