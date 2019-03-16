#Import from the PIL library and use routines from the Image module

from PIL import Image

#Import from the glob and os module

import glob, os

#Get your user declared input values for x and y

inX = input("Value for x: ")
inY = input("Value for y: ")

#Make sure that the input values are initialized as integers

x = int(inX)
y = int(inY)

#Use the size method to define the dimensions or size of the thumbnail

size = x, y

#Generate the thumbnails for the image or images in the folder
#The generated thumbnails will be in JPEG file format

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + "tb.JPG", "JPEG")
    

