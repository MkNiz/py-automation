from PIL import Image

kity = Image.open("kitty.jpg")

kityW, kityH = kity.size
print("kity.jpg has a width of", kityW, "and a height of", kityH)
print("This image's filename is", kity.filename)
print("It is of the", kity.format, "(", kity.format_description, ") format.")
