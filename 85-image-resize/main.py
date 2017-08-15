from PIL import Image

cat_icon = Image.open("cat_icon.png")
bigger_cat_icon = cat_icon.resize((128, 128))

bigger_cat_icon.save("large_cat_icon.png")
print("Image saved")