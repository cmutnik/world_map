# World Map of Photos 

Generate a map with pins that identify locations you have visited.  Clicking a pin causes an image, taken at the location, to pop-up.

----
### Photos Taken Around the World


----
### Icon Modifications
`folium` has various marker options.  A full list of icon options can be found on Front Awesome, [here.](https://fontawesome.com/v4.7.0/icons/)<br>
This project uses red icons with a picture symbol in them:
```py
[folium.Marker(
location=imgcoords[j],
popup=folium.Popup(testNOloop[j], max_width=imgsize),
icon=folium.Icon(color='red', icon='picture')
).add_to(m)  for j in range(len(imgcoords))]
```
If you wanted to add red markers with a different symbol in them, you can change the `icon` setting:
```py
[folium.Marker(
location=imgcoords[j],
popup=folium.Popup(testNOloop[j], max_width=imgsize),
icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)  for j in range(len(imgcoords))]
```
Here is another method to add markers (with default color and symbol):
```py
# use standard blue marker, with popup
popup1 = [folium.Popup(testNOloop[i], max_width=imgsize) for i in range(len(testNOloop))]
[folium.Marker(location=imgcoords[j], popup=popup1[j],).add_to(m) for j in range(len(imgcoords))]
```
To add a marker, without a popup:
```py
# add marker (no popup)
[folium.Marker(imgcoords[i]).add_to(m) for i in range(len(imgcoords))] 
```
