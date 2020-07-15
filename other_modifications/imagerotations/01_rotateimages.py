from PIL import ExifTags, Image

filename = './path/to/inimg.JPG'
output_fname = './outpath/to/outimg.JPG'


img = Image.open(filename)
#print(img._getexif().items())
exif=dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)

# check image orientation
print(exif['Orientation'])

if not exif['Orientation']:
    img=img.rotate(90, expand=True)
elif exif['Orientation']== 6:
    img=img.rotate(270, expand=True)
img.thumbnail((1000,1000), Image.ANTIALIAS)
img.save(output_fname, "JPEG")