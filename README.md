# Thumbnail View Generator

This generates a thumbnail preview for images.

This is a convenient way to allow smaller versions of an image to be shared, rather than uploading the full high resolution image. The higher quality version of an image takes up more space and bandwidth.

By generating a smaller preview file, it saves space and time to upload to the cloud or data center.

I made it more interactive to allow the user to declare the dimension of width and height of the image using the x and y values in the size method.

size = x, y

The x denotes the width and y denotes the height. So for a thumbnail preview of 300 x 300, the following arguments will be passed to the size method.

size = 300, 300

I created an input value for x and y to allow user to specify the size of the thumbnail.

The images that will be generated into a thumbnail must be placed in the same folder or directory as the thumbnails.py file that contains the code.
