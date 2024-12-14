# Create an interactive map using Python

import folium

location = (-34.6037,-58.3816)

map = folium.Map(location = location, zoom_start=12)

folium.Marker(location, popup='CABA').add_to(map)

map.save('map.html')