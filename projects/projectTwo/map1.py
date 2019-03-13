import folium
import webbrowser
import os

filename = 'Map1.html'
full_filename_path = os.path.realpath(filename)

map = folium.Map(location=[39.94, -75.14],
                 zoom_start=18)

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates,
                               popup="Hi I am a Marker",
                               icon=folium.Icon(color='green')
                               ))

map.add_child(fg)

map.save(filename)
webbrowser.open('file://' + full_filename_path)
