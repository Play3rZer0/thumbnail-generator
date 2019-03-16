from PIL import Image

import glob, os

inX = input("Value for x: ")
inY = input("Value for y: ")

x = int(inX)
y = int(inY)

size = x, y

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + "tb.JPG", "JPEG")
