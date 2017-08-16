from PIL import Image

kity = Image.open("kitty.jpg")

# Rotate, then save
kity.rotate(90, expand=True).save("kitty-r90.jpg")
print("Rotated image saved.")

# Flip, then save
kity.transpose(Image.FLIP_TOP_BOTTOM).save("kitty-vert-flip.jpg")
print("Flipped image saved.")