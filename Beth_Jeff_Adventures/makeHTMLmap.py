import folium

img1Path='./photos/IMG_0195.JPG'
img1coords=[42.3730, -73.3677]

m = folium.Map(img1coords, zoom_start=10)

#test = folium.Html('<b>Hello world</b>', script=True)
test = folium.Html('<img src='+img1Path+' alt="Italian Trulli">', script=True)

# add pin
folium.Marker(img1coords).add_to(m)

# add popup
popup1 = folium.Popup(test, max_width=2650)

folium.RegularPolygonMarker(
    location=img1coords, popup=popup1,
).add_to(m)

m.save('Beth_Jeff_Adventures.html')