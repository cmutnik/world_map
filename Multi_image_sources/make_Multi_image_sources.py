#!/usr/bin/python
# Corey Mutnik 200706
# Python script to turn all images in designated dir to thumbnails and plot them on a world map
# varibales in the main() need to be modified accordingly
from PIL import Image
import pandas as pd
import folium
import os

'''
TODO 
make sure all images in list exist in both photos and thumbnails dir
maybe leave off thumbnails not in photolist.csv

preserve photo aspect ratio

call lat/long from efix data?

Do polygon markers showup offline but icon markers dont or is it a cache issue?

at bottom of each function, print len of image set used: len(df), len(glob(path_to_thumbnails))
possibly set variables as global, to compare the len with '==':
global lendf = len(df)

'''


def main():
    '''
        Set the variables to be used 
            path names
            accepted image types
            image thumbnail sizes
            output name of map
    '''
    # path images stored in
    _path_to_original_images = './photos/originals/'

    # path you want thumbnails saved to
    _path_for_thumnails = './photos/thumbnails/'

    # name of final photo map file
    _mapname='Multi_image_sources.html'

    # thumbnail dimensions and size of boarder arund image (on photomap)
    _imgsize = 500

    # list of accepted image extensions
    _extensions = ('.jpg', '.JPG', '.jpeg', '.png', '.PNG')

    
    # call function to make thumbnails
    makeThumbnails(_path_to_original_images, _path_for_thumnails, _imgsize, _extensions)
    # call function to make photo map
    makePhotoMap(_mapname, _imgsize, _path_for_thumnails)


def makeThumbnails(path_to_original_images, path_for_thumnails, imgsize, extensions):
    ''' 
        Function to make thumbnails out of all images we want to add to the final page 
    '''
    # make directory for thumbnails, if it doesnt exist
    if not os.path.exists(path_for_thumnails):
        os.makedirs(path_for_thumnails)

    for photos in os.listdir(path_to_original_images):
        # only run loop over files that have correct extensions
        if photos.endswith(extensions):
            outFilename = path_for_thumnails + photos
            
            # check if thumbnail already exists
            if os.path.isfile(outFilename):
                print('Thumbnail already exists for: %s ' % photos)
            else:
                # open image
                img = Image.open(path_to_original_images + photos)

                #####
                # Make sure thumbnails are rotated correctly
                #####
                # use try to only apply code to images with exif data
                try:
                    # get orientation value from exif data
                    image_exif = img._getexif()
                    image_orientation = image_exif[274]

                    # rotate images based on orientation value
                    if image_orientation == 3:
                        img = img.rotate(180)
                    if image_orientation == 6:
                        img = img.rotate(-90)
                    if image_orientation == 8:
                        img = img.rotate(90)  
                except:
                    pass

                # once rotated, make a thumbnail of each image
                img.thumbnail([imgsize, imgsize],Image.ANTIALIAS)

                # save ouput image
                img.save(outFilename)
                
                print('thumbnail made for: %s' % photos)
        else:
            #print(photos + ' doesnt have the correct extension, a thumbnail was not made')
            print('thumbnail not made for: %s' % photos)

#def makePhotoMap(mapname='./Beth_Jeff_Adventures_thumbnails.html'):
def makePhotoMap(mapname, imgsize, path_for_thumnails):
    '''
        Function to take all images from list and add them to photo map
    '''
    # initialize map
    m = folium.Map([42.3730,-73.3677], zoom_start=3, tiles='Stamen Terrain')
    
    def addimagestomap(df, pincolor):
        # append thumbnail directory to image names
        df[df.columns[0]] = path_for_thumnails + df[df.columns[0]]
        # make list out of photos
        imgpaths=df[df.columns[0]].to_list()
        
        # batch coordinates for each image
        imgcoords=[[df[df.columns[1]][i], df[df.columns[2]][i]] for i in range(len(df))]

        testNOloop = [folium.Html('<img src='+imgpaths[i]+'>', script=True) for i in range(len(imgpaths))]   
        
        #####
        # add marker for each popup
        #####
        [folium.Marker(
        location=imgcoords[j],
        popup=folium.Popup(testNOloop[j], max_width=imgsize),
        #icon=folium.Icon(color='green')
        icon=folium.Icon(color=pincolor, icon='picture')
        ).add_to(m)  for j in range(len(imgcoords))]

        counter = len(imgcoords)
        return print(counter, ' ' + pincolor + ' pins added')
    

    ################################################################
    ##### Use Different Color Pins to Distinguish Photos Owner #####
    ################################################################
    
    # do for all images in dukes image file
    df_dukes = pd.read_csv('./photos/dukesPics.csv')
    # add dukes images to map
    addimagestomap(df=df_dukes, pincolor='red')
    
    # do for all images in takos image file
    df_tako = pd.read_csv('./photos/TakosPics.csv')
    # add takos images to map
    addimagestomap(df=df_tako, pincolor='green')

    # save completed map
    m.save(mapname)
    
    return print(mapname + ' was made')


# call function to make tumbnails and load them onto a map
main()