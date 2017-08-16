from PIL import Image, ImageDraw

img = Image.new('RGBA', (320, 240), 'white')
draw = ImageDraw.Draw(img)

# Draw points
for pY in range(0, 240, 2):
    draw.point((3, pY), (128, 128, 128, 255))
    draw.point((315, pY), (128, 128, 128, 255))

# Draw lines
draw.line([(0, 2), (319, 2)], (200, 64, 64, 255), 1)
draw.line([(0, 236), (319, 236)], (200, 64, 64, 255), 1)

# Draw rectangle
draw.rectangle((5, 5, 313, 233), (255, 0, 0, 255), (0, 0, 0, 255))

# Draw ellipse
draw.ellipse((38, 9, 280, 229), (0, 255, 0, 255))

# Draw polygon
draw.polygon([(159, 9), (38, 229), (280, 229)], (0, 0, 255, 255))

img.save("shapes.png")
print("File saved")