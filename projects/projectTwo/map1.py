import folium
import webbrowser
import os
import pandas


data = pandas.read_csv('volcanoe_data.txt')
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if 1000 > elevation:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[39.94, -75.14],
                 zoom_start=18)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                      radius=6,
                                      popup=str(el) + " m",
                                      fill_color=color_producer(el),
                                      color='grey',
                                      fill_opacity=0.7
                                      ))

fgp = folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(
    data=(open("world.json", "r", encoding="utf-8-sig").read()),
    style_function=lambda x: {'fillColor': "green" if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}
))

# popupText = ["Hi I am a Marker", "Second popup text"]
# iconColor = ["green", "blue"]
# for coordinates in [[39.94, -75.14], [39.2, -97.1]]:
#     fg.add_child(folium.Marker(location=coordinates,
#                                popup='popupText',
#                                icon=folium.Icon(color=color_producer(el))
#                                ))


# print('from map1.py printing the coordinates ---> ', coordinates)


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
filename = 'Map1.html'
full_filename_path = os.path.realpath(filename)

map.save(filename)
webbrowser.open('file://' + full_filename_path)
