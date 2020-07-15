from PIL import Image, ExifTags

# open image
image = Image.open('./path/to/image.jpg')

# use try to only apply code to images with exif data
try:
    # get orientation value from exif data
    image_exif = image._getexif()
    image_orientation = image_exif[274]

    # rotate images based on orientation value
    if image_orientation == 3:
        rotated = image.rotate(180)
    if image_orientation == 6:
        rotated = image.rotate(-90)
    if image_orientation == 8:
        rotated = image.rotate(90)

    # save image
    rotated.save('outimg.jpg')
except:
    pass

