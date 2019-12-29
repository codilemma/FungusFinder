import requests
import urllib
import json
import itertools
import pandas as pd
import folium
from folium.plugins import MarkerCluster

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from branca.element import Template, MacroElement

from legends_templates import march_template, march_terrain_template
from legends_templates import april_template, april_terrain_template
from legends_templates import may_template, may_terrain_template
from legends_templates import june_template, june_terrain_template
from legends_templates import july_template, july_terrain_template

def map_fires(el_max,el_min,map_month,
            df_fires_16_V1,df_fires_16_M6,df_fires_17_V1,df_fires_17_M6,
            df_fires_18_V1,df_fires_18_M6,df_fires_19_V1,df_fires_19_M6,
            locationlist_16_V1,locationlist_16_M6,locationlist_17_V1,locationlist_17_M6,
            locationlist_18_V1,locationlist_18_M6,locationlist_19_V1,locationlist_19_M6):
    map = folium.Map(location=[45.5051,-122.6750], zoom_start=12, 
                     title=f"2016-2019 Fire Data Map for {map_month} Hunting, {str(el_min)}ft to {str(el_max)} elevations")
    mcluster_16_V1 = MarkerCluster().add_to(map)
    mcluster_16_M6 = MarkerCluster().add_to(map)
    mcluster_17_V1 = MarkerCluster().add_to(map)
    mcluster_17_M6 = MarkerCluster().add_to(map)
    mcluster_18_V1 = MarkerCluster().add_to(map)
    mcluster_18_M6 = MarkerCluster().add_to(map)
    mcluster_19_V1 = MarkerCluster().add_to(map)
    mcluster_19_M6 = MarkerCluster().add_to(map)

    for point in range(0,len(locationlist_16_V1)):
        if (el_max >= df_fires_16_V1['elevation'][point] >= el_min):
            folium.Marker(locationlist_16_V1[point], 
                          popup=df_fires_16_V1['label'][point],
                          icon=folium.Icon(color='green',icon='fire')
                          ).add_to(mcluster_16_V1)

    for point in range(0,len(locationlist_16_M6)):
        if (el_max >= df_fires_16_M6['elevation'][point] >= el_min):
            folium.Marker(locationlist_16_M6[point], 
                          popup=df_fires_16_M6['label'][point],
                          icon=folium.Icon(color='green',icon='fire')
                          ).add_to(mcluster_16_M6)

    for point in range(0,len(locationlist_17_V1)):
        if (el_max >= df_fires_17_V1['elevation'][point] >= el_min):
            folium.Marker(locationlist_17_V1[point], 
                          popup=df_fires_17_V1['label'][point],
                          icon=folium.Icon(color='pink',icon='fire')
                          ).add_to(mcluster_17_V1)

    for point in range(0,len(locationlist_17_M6)):
        if (el_max >= df_fires_17_M6['elevation'][point] >= el_min):
            folium.Marker(locationlist_17_M6[point], 
                          popup=df_fires_17_M6['label'][point],
                          icon=folium.Icon(color='pink',icon='fire')
                          ).add_to(mcluster_17_M6)

    for point in range(0,len(locationlist_18_V1)):
        if (el_max >= df_fires_18_V1['elevation'][point] >= el_min):
            folium.Marker(locationlist_18_V1[point], 
                          popup=df_fires_18_V1['label'][point],
                          icon=folium.Icon(color='orange',icon='fire')
                          ).add_to(mcluster_18_V1)

    for point in range(0,len(locationlist_18_M6)):
        if (el_max >= df_fires_18_M6['elevation'][point] >= el_min):
            folium.Marker(locationlist_18_M6[point], 
                          popup=df_fires_18_M6['label'][point],
                          icon=folium.Icon(color='orange',icon='fire')
                          ).add_to(mcluster_18_M6)

    for point in range(0,len(locationlist_19_V1)):
        if (el_max >= df_fires_19_V1['elevation'][point] >= el_min):
            folium.Marker(locationlist_19_V1[point], 
                          popup=df_fires_19_V1['label'][point],
                          icon=folium.Icon(color='red',icon='fire')
                          ).add_to(mcluster_19_V1)

    for point in range(0,len(locationlist_19_M6)):
        if (el_max >= df_fires_19_M6['elevation'][point] >= el_min):
            folium.Marker(locationlist_19_M6[point], 
                          popup=df_fires_19_M6['label'][point],
                          icon=folium.Icon(color='red',icon='fire')
                          ).add_to(mcluster_19_M6)

    if (map_month == "March"):
        template = march_template
    elif(map_month == "April"):
        template = april_template
    elif(map_month == "May"):
        template = may_template
    elif(map_month == "June"):
        template = june_template
    elif(map_month == "July"):
        template = july_template

    macro = MacroElement()
    macro._template = Template(template)

    map.get_root().add_child(macro)
    map.save(f"html_maps/fire_map_{map_month}.html")

    map2 = folium.Map(location=[45.5051,-122.6750], tiles='Stamen Terrain',zoom_start=12, 
                        title=f"2016-2019 Fire Data Terrain Map for {map_month} Hunting, {str(el_min)}ft to {str(el_max)} elevations")
    mcluster_16_V1 = MarkerCluster().add_to(map2)
    mcluster_16_M6 = MarkerCluster().add_to(map2)
    mcluster_17_V1 = MarkerCluster().add_to(map2)
    mcluster_17_M6 = MarkerCluster().add_to(map2)
    mcluster_18_V1 = MarkerCluster().add_to(map2)
    mcluster_18_M6 = MarkerCluster().add_to(map2)
    mcluster_19_V1 = MarkerCluster().add_to(map2)
    mcluster_19_M6 = MarkerCluster().add_to(map2)

    for point in range(0,len(locationlist_16_V1)):
        if (el_max >= df_fires_16_V1['elevation'][point] >= el_min):
            folium.Marker(locationlist_16_V1[point], 
                          popup=df_fires_16_V1['label'][point],
                          icon=folium.Icon(color='green',icon='fire')
                          ).add_to(mcluster_16_V1)

    for point in range(0,len(locationlist_16_M6)):
        if (el_max >= df_fires_16_M6['elevation'][point] >= el_min):
            folium.Marker(locationlist_16_M6[point], 
                          popup=df_fires_16_M6['label'][point],
                          icon=folium.Icon(color='green',icon='fire')
                          ).add_to(mcluster_16_M6)

    for point in range(0,len(locationlist_17_V1)):
        if (el_max >= df_fires_17_V1['elevation'][point] >= el_min):
            folium.Marker(locationlist_17_V1[point], 
                          popup=df_fires_17_V1['label'][point],
                          icon=folium.Icon(color='pink',icon='fire')
                          ).add_to(mcluster_17_V1)

    for point in range(0,len(locationlist_17_M6)):
        if (el_max >= df_fires_17_M6['elevation'][point] >= el_min):
            folium.Marker(locationlist_17_M6[point], 
                          popup=df_fires_17_M6['label'][point],
                          icon=folium.Icon(color='pink',icon='fire')
                          ).add_to(mcluster_17_M6)

    for point in range(0,len(locationlist_18_V1)):
        if (el_max >= df_fires_18_V1['elevation'][point] >= el_min):
            folium.Marker(locationlist_18_V1[point], 
                          popup=df_fires_18_V1['label'][point],
                          icon=folium.Icon(color='orange',icon='fire')
                          ).add_to(mcluster_18_V1)

    for point in range(0,len(locationlist_18_M6)):
        if (el_max >= df_fires_18_M6['elevation'][point] >= el_min):
            folium.Marker(locationlist_18_M6[point], 
                          popup=df_fires_18_M6['label'][point],
                          icon=folium.Icon(color='orange',icon='fire')
                          ).add_to(mcluster_18_M6)

    for point in range(0,len(locationlist_19_V1)):
        if (el_max >= df_fires_19_V1['elevation'][point] >= el_min):
            folium.Marker(locationlist_19_V1[point], 
                          popup=df_fires_19_V1['label'][point],
                          icon=folium.Icon(color='red',icon='fire')
                          ).add_to(mcluster_19_V1)

    for point in range(0,len(locationlist_19_M6)):
        if (el_max >= df_fires_19_M6['elevation'][point] >= el_min):
            folium.Marker(locationlist_19_M6[point], 
                          popup=df_fires_19_M6['label'][point],
                          icon=folium.Icon(color='red',icon='fire')
                          ).add_to(mcluster_19_M6)

    if (map_month == "March"):
        template = march_terrain_template
    elif(map_month == "April"):
        template = april_terrain_template
    elif(map_month == "May"):
        template = may_terrain_template
    elif(map_month == "June"):
        template = june_terrain_template
    elif(map_month == "July"):
        template = july_terrain_template
        
    macro = MacroElement()
    macro._template = Template(template)

    map2.get_root().add_child(macro)
    map2.save(f"html_maps/fire_map_{map_month}_Terrain.html")

# Extract the Fire data frames from the Json Files\
fire_data_16_V1 = 'fire_data/filtered_fire_data_16_V1.json'
fire_data_16_M6 = 'fire_data/filtered_fire_data_16_M6.json'
fire_data_17_V1 = 'fire_data/filtered_fire_data_17_V1.json'
fire_data_17_M6 = 'fire_data/filtered_fire_data_17_M6.json'
fire_data_18_V1 = 'fire_data/filtered_fire_data_18_V1.json'
fire_data_18_M6 = 'fire_data/filtered_fire_data_18_M6.json'
fire_data_19_V1 = 'fire_data/filtered_fire_data_19_V1.json'
fire_data_19_M6 = 'fire_data/filtered_fire_data_19_M6.json'

df_fires_16_V1 = pd.read_json(fire_data_16_V1)
df_fires_16_M6 = pd.read_json(fire_data_16_M6)
df_fires_17_V1 = pd.read_json(fire_data_17_V1)
df_fires_17_M6 = pd.read_json(fire_data_17_M6)
df_fires_18_V1 = pd.read_json(fire_data_18_V1)
df_fires_18_M6 = pd.read_json(fire_data_18_M6)
df_fires_19_V1 = pd.read_json(fire_data_19_V1)
df_fires_19_M6 = pd.read_json(fire_data_19_M6)

# Create a list of all fire locations
locations_16_V1 = df_fires_16_V1[['lat','lon']]
locationlist_16_V1 = locations_16_V1.values.tolist()
locations_16_M6 = df_fires_16_M6[['lat','lon']]
locationlist_16_M6 = locations_16_M6.values.tolist()

locations_17_V1 = df_fires_17_V1[['lat','lon']]
locationlist_17_V1 = locations_17_V1.values.tolist()
locations_17_M6 = df_fires_17_M6[['lat','lon']]
locationlist_17_M6 = locations_17_M6.values.tolist()

locations_18_V1 = df_fires_18_V1[['lat','lon']]
locationlist_18_V1 = locations_18_V1.values.tolist()
locations_18_M6 = df_fires_18_M6[['lat','lon']]
locationlist_18_M6 = locations_18_M6.values.tolist()

locations_19_V1 = df_fires_19_V1[['lat','lon']]
locationlist_19_V1 = locations_19_V1.values.tolist()
locations_19_M6 = df_fires_19_M6[['lat','lon']]
locationlist_19_M6 = locations_19_M6.values.tolist()

## Map the Fires for March Hunting between elevations of 300ft and 1500ft
el_max = 1500
el_min = 300
map_month = "March"
map_fires(el_max,el_min,map_month,
            df_fires_16_V1,df_fires_16_M6,df_fires_17_V1,df_fires_17_M6,
            df_fires_18_V1,df_fires_18_M6,df_fires_19_V1,df_fires_19_M6,
            locationlist_16_V1,locationlist_16_M6,locationlist_17_V1,locationlist_17_M6,
            locationlist_18_V1,locationlist_18_M6,locationlist_19_V1,locationlist_19_M6)

# Map the Fires for April between elevations of 1500ft and 3500ft
el_max = 3500
el_min = 1500
map_month = "April"
map_fires(el_max,el_min,map_month,
            df_fires_16_V1,df_fires_16_M6,df_fires_17_V1,df_fires_17_M6,
            df_fires_18_V1,df_fires_18_M6,df_fires_19_V1,df_fires_19_M6,
            locationlist_16_V1,locationlist_16_M6,locationlist_17_V1,locationlist_17_M6,
            locationlist_18_V1,locationlist_18_M6,locationlist_19_V1,locationlist_19_M6)

## Map the Fires for May between elevations of 3500ft and 5000ft
el_max = 5000
el_min = 3500
map_month = "May"
map_fires(el_max,el_min,map_month,
            df_fires_16_V1,df_fires_16_M6,df_fires_17_V1,df_fires_17_M6,
            df_fires_18_V1,df_fires_18_M6,df_fires_19_V1,df_fires_19_M6,
            locationlist_16_V1,locationlist_16_M6,locationlist_17_V1,locationlist_17_M6,
            locationlist_18_V1,locationlist_18_M6,locationlist_19_V1,locationlist_19_M6)

## Map the Fires for June between elevations of 4500ft and 6500ft
el_max = 6500
el_min = 4500
map_month = "June"
map_fires(el_max,el_min,map_month,
            df_fires_16_V1,df_fires_16_M6,df_fires_17_V1,df_fires_17_M6,
            df_fires_18_V1,df_fires_18_M6,df_fires_19_V1,df_fires_19_M6,
            locationlist_16_V1,locationlist_16_M6,locationlist_17_V1,locationlist_17_M6,
            locationlist_18_V1,locationlist_18_M6,locationlist_19_V1,locationlist_19_M6)

## Map the Fires for July between elevations of 6000ft and 8000ft
el_max = 8000
el_min = 6000
map_month = "July"
map_fires(el_max,el_min,map_month,
            df_fires_16_V1,df_fires_16_M6,df_fires_17_V1,df_fires_17_M6,
            df_fires_18_V1,df_fires_18_M6,df_fires_19_V1,df_fires_19_M6,
            locationlist_16_V1,locationlist_16_M6,locationlist_17_V1,locationlist_17_M6,
            locationlist_18_V1,locationlist_18_M6,locationlist_19_V1,locationlist_19_M6)

