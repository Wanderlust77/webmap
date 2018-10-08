import folium
map=folium.Map(location=[55.932090, -3.168233], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")

fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)



map.save("Map1.html")
