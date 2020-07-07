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
    _path_to_original_images = './photos/'

    # path you want thumbnails saved to
    _path_for_thumnails = './thumbnails/'

    # name of final photo map file
    _mapname='Beth_Jeff_Adventures_thumbnails.html'

    # thumbnail dimensions and size of boarder arund image (on photomap)
    _imgsize = 500

    # list of accepted image extensions
    _extensions = ('.jpg', '.JPG', '.png', '.PNG')

    
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
        #if photos.endswith(".jpg") or photos.endswith(".JPG") or photos.endswith(".png") or photos.endswith(".PNG"):
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

#def makePhotoMap(mapname='./Beth_Jeff_Adventures_thumbnails.html'):
def makePhotoMap(mapname, imgsize, path_for_thumnails):
    '''
        Function to take all images from list and add them to photo map
    '''
    # do for all images in file, not just one image
    df = pd.read_csv('photolist_nopath.csv')
    # append thumbnail directory to image names
    df[df.columns[0]] = path_for_thumnails + df[df.columns[0]]
    # make list out of photos
    imgpaths=df[df.columns[0]].to_list()
    
    # batch coordinates for each image
    #imgcoords=[[df['lat'][i], df['long'][i]] for i in range(len(df))]
    imgcoords=[[df[df.columns[1]][i], df[df.columns[2]][i]] for i in range(len(df))]

    # make list of image descriptions
    #describeimgs=df[df.columns[3]].to_list()

    m = folium.Map(imgcoords[0], zoom_start=10)

    testNOloop = [folium.Html('<img src='+imgpaths[i]+'>', script=True) for i in range(len(imgpaths))]   
    
    #####
    # add marker for each popup
    #####
    # add marker (no popup)
    #[folium.Marker(imgcoords[i]).add_to(m) for i in range(len(imgcoords))] 
    # use a regular polygon as a marker, with popup
    #[folium.RegularPolygonMarker(location=imgcoords[j], popup=popup1[j],).add_to(m) for j in range(len(imgcoords))]
    # use standard blue marker, with popup
    #popup1 = [folium.Popup(testNOloop[i], max_width=imgsize) for i in range(len(testNOloop))]
    #[folium.Marker(location=imgcoords[j], popup=popup1[j],).add_to(m) for j in range(len(imgcoords))]
    # 
    [folium.Marker(
    location=imgcoords[j],
    popup=folium.Popup(testNOloop[j], max_width=imgsize),
    #icon=folium.Icon(color='green')
    icon=folium.Icon(color='red', icon='picture')
    ).add_to(m)  for j in range(len(imgcoords))]

    m.save(mapname)

    return print(mapname + ' was made')


# call function to make tumbnails and load them onto a map
main()