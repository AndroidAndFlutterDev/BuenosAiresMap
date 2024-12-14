# Create an interactive map using Python

import folium

# Buenos Aires location (you can choose whatever you want, like New York)
location = (-34.6037,-58.3816)

map = folium.Map(location = location, zoom_start=12)

# Add the marker to the map
folium.Marker(location, popup='CABA').add_to(map)

# Save it as map.html
map.save('map.html')

print("The map.html has been generated. Open it in your browser")
