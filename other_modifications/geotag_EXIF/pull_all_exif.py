from PIL import ExifTags, Image

# set input image location
filename = './path/to/inimg.JPG'

# open image
img = Image.open(filename)
#print(img._getexif().items())

# pull all the exif data
exif=dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)

# print all exif data associated with the image
print(exif)
