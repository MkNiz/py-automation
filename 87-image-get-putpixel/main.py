from PIL import Image

def add_cv(initial, amt):
    """Adds amt to initial, but limits the value to 255"""
    assert(amt >= 0)
    total = initial + amt
    return (total <= 255 and total) or 255

def sub_cv(initial, amt):
    """Subtracts amt from initial, but will not drop below 0"""
    assert(amt >= 0)
    total = initial - amt
    return (total >= 0 and total) or 0

kity = Image.open("kitty.jpg")
kW, kH = kity.size

# Make all pixels more red and less green
for pY in range(kH):
    for pX in range(kW):
        # Get current pixel color values
        pR, pG, pB, pA = kity.getpixel((pX, pY))
        print("Pixel at ({0}, {1}) has color value ({2}, {3}, {4}, {5}).".format(pX, pY, pR, pG, pB, pA))
        
        # Set with 25 more red and 30 less green
        kity.putpixel((pX, pY), (add_cv(pR, 25), sub_cv(pG, 30), pB, pA))
        pnR, pnG, pnB, pnA = kity.getpixel((pX, pY))
        print("({0}, {1}) has been changed to ({2}, {3}, {4}, {5}).".format(pX, pY, pnR, pnG, pnB, pnA))

kity.save("kitty-colorized.png")
print("\nFile saved")