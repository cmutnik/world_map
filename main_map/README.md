# Photo Map
This method uses photo data stored in a csv file.

[`unfinished_map.py`](./unfinished_map.py) plots the photos listed in [`photolist_nopath.csv`](./photolist_nopath.csv).  First, images are resized and then plotted on a world map.

----
### To Add
Explain how code works (functions called and what they do).  Show screenshot example of output.

Do polygon markers showup offline but icon markers dont or is it a cache issue?
T
----
----
## Function Breakdown
This section will discuss how the code works, describing how and why each function is used.

----
### main()
----
### `makeThumbnails()`
Using inputs from the function `main()`, `makeThumbnails()` makes thumbnails out of all images we want to add to the final page.
```py
def makeThumbnails(path_to_original_images, path_for_thumnails, imgsize, extensions):
```
Check to see if the thumbnail directory exists.  If it doesn't exist, make one.
```py
    if not os.path.exists(path_for_thumnails):
        os.makedirs(path_for_thumnails)
```
Loop through all items in the original image directory.  Skip all images that already have a corresponding thumbnail.  Make a thumbnail for all other images.
```py
    for photos in os.listdir(path_to_original_images):
        # only run loop over files that have correct extensions
        if photos.endswith(extensions):
            outFilename = path_for_thumnails + photos
            
            # check if thumbnail already exists
            if os.path.isfile(outFilename):
                print('Thumbnail already exists for: ', photos)
            else:
                # open and resize images     
                img = Image.open(path_to_original_images + photos)
                img.thumbnail([imgsize, imgsize],Image.ANTIALIAS)

                # save ouput file
                img.save(outFilename)
                
                print('thumbnail made for: ', photos)
        else:
            #print(photos + ' doesnt have the correct extension, a thumbnail was not made')
            print('thumbnail not made for: ', photos)
```

----
### makePhotoMap()