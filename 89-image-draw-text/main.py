from PIL import Image, ImageDraw, ImageFont
import os

img = Image.new('RGBA', (320, 240), 'white')
draw = ImageDraw.Draw(img)

# Draw text with default font
draw.text((15, 15), "I DREW THIS TEXT,\nEAT IT", fill='black')

# Get font folder (on a mac, Library/Fonts).
# Set this with a font on your system
fontDir = '/Library/Fonts'
fontC64 = ImageFont.truetype(os.path.join(fontDir, 'c64.ttf'), 12)

draw.text((63, 63), "Ain't that swell?", fill='purple', font=fontC64)

img.save("draw_text.png")
print("Saved image")