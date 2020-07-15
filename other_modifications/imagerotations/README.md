# Rotating Images
When creating thumbnails, some images are returned with an incorrect orientation.  To correct this, EXIF data needs to be retrieved from each image and used to rotate them accordingly.  This must be done before a thumbnail is saved, since EXIF data is not passed along to the thumbnail files.

[`00_rotateimages.py`](./00_rotateimages.py) shows one method to rotate images.  This script only uses `image_orientation` values of `3`, `6`, and `8`.  Below is a full list of `image_orientation` and their required corrections.

```py
exif_transpose_sequences = [                   # Val  0th row  0th col
    [],                                        #  0    (reserved)
    [],                                        #  1   top      left
    [Image.FLIP_LEFT_RIGHT],                   #  2   top      right
    [Image.ROTATE_180],                        #  3   bottom   right
    [Image.FLIP_TOP_BOTTOM],                   #  4   bottom   left
    [Image.FLIP_LEFT_RIGHT, Image.ROTATE_90],  #  5   left     top
    [Image.ROTATE_270],                        #  6   right    top
    [Image.FLIP_TOP_BOTTOM, Image.ROTATE_90],  #  7   right    bottom
    [Image.ROTATE_90],                         #  8   left     bottom
]
```

The rotation values listed above can be implemented using the following code:
```py
if not exif['Orientation']:
    img=img.rotate(90, expand=True)
elif exif['Orientation'] == 2:
    img=img.FLIP_LEFT_RIGHT
elif exif['Orientation'] == 3:
    img=img.rotate(180, expand=True)
elif exif['Orientation'] == 4:
    img=img.FLIP_TOP_BOTTOM
elif exif['Orientation'] == 5:
    img=img.rotate(90, expand=True)
elif exif['Orientation'] == 6:
    img=img.rotate(270, expand=True)
elif exif['Orientation'] == 7:
    img=img.rotate(90, expand=True)
elif exif['Orientation'] == 8:
    img=img.rotate(90, expand=True)
```