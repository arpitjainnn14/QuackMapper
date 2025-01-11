import folium
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('earthquakes_real.csv')

# Create a world map centered at the equator and prime meridian
world_map = folium.Map(location=[0, 0], zoom_start=2)

# Iterate over the rows of the DataFrame and add markers
for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Place']).add_to(world_map)

# Save the map as an HTML file
world_map.save('world_map_with_markers.html')


