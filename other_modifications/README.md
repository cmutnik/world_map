# Other Modifications

This directory contains other options for modifying a photo map.

The subdirectory [`geotag_EFIX/`](./other_modifications/geotag_EFIX/) is used to extract location data from a photos EFIX.  This data is used to automatically plot photos, without the need for a `*.csv` file.
```py
from PIL import ExifTags, Image

# set input image location
filename = './path/to/inimg.JPG'

# open image
img = Image.open(filename)

# pull all the exif data
exif=dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)

# print all exif data associated with the image
print(exif)
```


The subdirectory [`imagerotations/`](./other_modifications/imagerotations/) uses exif data to ensure thumbnails are generated with proper orientation.  If this is not used, some image popups will be displayed with a $90\deg$ rotation.
```py
from PIL import ExifTags, Image

filename = './path/to/inimg.JPG'
output_fname = './outpath/to/outimg.JPG'

img = Image.open(filename)

exif=dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)

# check image orientation
print(exif['Orientation'])

if not exif['Orientation']:
    img=img.rotate(90, expand=True)
elif exif['Orientation']== 6:
    img=img.rotate(270, expand=True)
img.thumbnail((1000,1000), Image.ANTIALIAS)
img.save(output_fname, "JPEG")
```