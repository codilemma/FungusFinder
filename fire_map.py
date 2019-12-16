import requests
import urllib
import json
import itertools
import pandas as pd
import folium
from folium.plugins import MarkerCluster

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Extract the Fire data frames from the Json Files\
fire_data_18_V1 = 'fire_data/readable_fire_data_18_V1.json'
fire_data_18_M6 = 'fire_data/fire_data_18_M6.json'
fire_data_19_V1 = 'fire_data/fire_data_19_V1.json'
fire_data_19_M6 = 'fire_data/fire_data_19_M6.json'

df_fires_18_V1 = pd.read_json(fire_data_18_V1)
df_fires_18_M6 = pd.read_json(fire_data_18_M6)
df_fires_19_V1 = pd.read_json(fire_data_19_V1)
df_fires_19_M6 = pd.read_json(fire_data_19_M6)

# Create a list of all fire locations
locations_18_V1 = df_fires_18_V1[['lat','lon']]
locationlist_18_V1 = locations_18_V1.values.tolist()

locations_18_M6 = df_fires_18_M6[['lat','lon']]
locationlist_18_M6 = locations_18_M6.values.tolist()


## Map the Fires
map = folium.Map(location=[45.5051,-122.6750], zoom_start=12)
marker_cluster1 = MarkerCluster().add_to(map)
marker_cluster2 = MarkerCluster().add_to(map)

for point in range(0,len(locationlist_18_V1)):
    folium.Marker(locationlist_18_V1[point], 
                  popup=df_fires_18_V1['label'][point],
                  icon=folium.Icon(color='red',icon='fire')
                  ).add_to(marker_cluster1)

for point in range(0,len(locationlist_18_M6)):
    folium.Marker(locationlist_18_M6[point], 
                  popup=df_fires_18_M6['label'][point],
                  icon=folium.Icon(color='orange',icon='fire')
                  ).add_to(marker_cluster2)
map.save('html_maps/fire_map_test.html')

#map2 = folium.Map(location=[45.5051,-122.6750], tiles='Stamen Terrain',zoom_start=12)
#marker_cluster = MarkerCluster().add_to(map2)
#for point in range(0,len(locationlist_19)):
#    folium.Marker(locationlist_19[point], popup=df_fires_19['label'][point]).add_to(marker_cluster)
#map2.save('html_maps/fire_map_terrain.html')

#map3 = folium.Map(location=[45.5051,-122.6750], zoom_start=12)
#marker_cluster = MarkerCluster().add_to(map3)
#for point in range(0,len(locationlist_18)):
#    folium.Marker(locationlist_18[point], popup=df_fires_18['label'][point]).add_to(marker_cluster)
#map3.save('fire_map_18.html')
#
#map4 = folium.Map(location=[45.5051,-122.6750], tiles='Stamen Terrain',zoom_start=12)
#marker_cluster = MarkerCluster().add_to(map2)
#for point in range(0,len(locationlist_18)):
#    folium.Marker(locationlist_18[point], popup=df_fires_18['label'][point]).add_to(marker_cluster)
#map4.save('fire_map2_18.html')
## Map the fires
#data = [{
#    'type':'scattergeo',
#    'lon': lons_19,
#    'lat': lats_19,
#    'text':labels_19,
#}]
#
#my_layout = Layout(title="2019 USA Fire Data",
#    )
#
#fig = {'data':data,'layout':my_layout}
#offline.plot(fig,filename='2019_usa_fire_map.html')