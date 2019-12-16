import json
import pandas as pd
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from get_elevation import get_elevation

from pandas import DataFrame

# Extract fire data from json file
fire_data_18_filename = '/home/code/WS/FungusFinderFireData/usa_fires_2018_archive_V1_90792.json'
with open(fire_data_18_filename) as f:
    all_fire_data_18 = json.load(f)

# Make a list of the date, lon, and latitude
# Filter data to only show fires in Oregon/Washington
dates_18, lats_18, lons_18, labels_18, elevations_18 = [], [], [], [], []
for fire_data_18 in all_fire_data_18:
    date_18 = fire_data_18['acq_date']
    lat_18 = fire_data_18['latitude']
    lon_18 = fire_data_18['longitude']
    if (-115 >= lon_18 >= -120) and (46 >= lat_18 >= 42):
        # get elevations and filter for optimal fungus growth
        try:
            elevation_18 = get_elevation(lat_18,lon_18)
        except ConnectionError:
            elevation_18 = 0
        print(elevation_18)
        dates_18.append(date_18)
        lats_18.append(lat_18)
        lons_18.append(lon_18)

        label_18 = f"Date: {date_18}\
            <br />Lat: {lat_18}\
            <br />Lon: {lon_18}\
            <br />El.: {elevation_18}"
        labels_18.append(label_18)

# Store the data in a Data Frame
df_fires_18_V1 = pd.DataFrame(
    {'date':dates_18,
     'lat':lats_18,
     'lon':lons_18,
     'label':labels_18
    }
)

# Store the Data Fram in a json file
df_fires_18_V1.to_json('fire_data/fire_data_18_V1.json')

# convert machine generated json into human readable format
filename = 'fire_data/fire_data_18_V1.json'
with open(filename) as f:
    fire_data = json.load(f)

readable_file = 'fire_data/readable_fire_data_18_V1.json'
with open(readable_file, 'w') as f:
    json.dump(fire_data,f,indent=4)

# Extract fire data from json file
fire_data_18_filename = '/home/code/WS/FungusFinderFireData/usa_fires_2018_archive_M6_90791.json'
with open(fire_data_18_filename) as f:
    all_fire_data_18 = json.load(f)

# Make a list of the date, lon, and latitude
# Filter data to only show fires in Oregon/Washington
dates_18, lats_18, lons_18, labels_18, elevations_18 = [], [], [], [], []
for fire_data_18 in all_fire_data_18:
    date_18 = fire_data_18['acq_date']
    lat_18 = fire_data_18['latitude']
    lon_18 = fire_data_18['longitude']
    if (-115 >= lon_18 >= -120) and (46 >= lat_18 >= 42):
        # get elevations and filter for optimal fungus growth
        try:
            elevation_18 = get_elevation(lat_18,lon_18)
        except ConnectionError:
            elevation_18 = 0
        print(elevation_18)
        dates_18.append(date_18)
        lats_18.append(lat_18)
        lons_18.append(lon_18)

        label_18 = f"Date: {date_18}\
            <br />Lat: {lat_18}\
            <br />Lon: {lon_18}\
            <br />El.: {elevation_18}"
        labels_18.append(label_18)

# Store the data in a Data Frame
df_fires_18_M6 = pd.DataFrame(
    {'date':dates_18,
     'lat':lats_18,
     'lon':lons_18,
     'label':labels_18
    }
)

# Store the Data Fram in a json file
df_fires_18_M6.to_json('fire_data/fire_data_18_M6.json')

# convert machine generated json into human readable format
filename = 'fire_data/fire_data_18_M6.json'
with open(filename) as f:
    fire_data = json.load(f)

readable_file = 'fire_data/readable_fire_data_18_M6.json'
with open(readable_file, 'w') as f:
    json.dump(fire_data,f,indent=4)

# ----------------------------------
# 2019 Data
# ----------------------------------

# Extract fire data from json file
fire_data_19_filename = '/home/code/WS/FungusFinderFireData/usa_fires_2019_archive_V1_90790.json'
with open(fire_data_19_filename) as f:
    all_fire_data_19 = json.load(f)

# Make a list of the date, lon, and latitude
# Filter data to only show fires in Oregon/Washington
dates_19, lats_19, lons_19, labels_19, elevations_19 = [], [], [], [], []
for fire_data_19 in all_fire_data_19:
    date_19 = fire_data_19['acq_date']
    lat_19 = fire_data_19['latitude']
    lon_19 = fire_data_19['longitude']
    if (-115 >= lon_19 >= -120) and (46 >= lat_19 >= 42):
        # get elevations and filter for optimal fungus growth
        try:
            elevation_19 = get_elevation(lat_19,lon_19)
        except ConnectionError:
            elevation_19 = 0
        print(elevation_19)
        dates_19.append(date_19)
        lats_19.append(lat_19)
        lons_19.append(lon_19)

        label_19 = f"Date: {date_19}\
            <br />Lat: {lat_19}\
            <br />Lon: {lon_19}\
            <br />El.: {elevation_19}"
        labels_19.append(label_19)

# Store the data in a Data Frame
df_fires_19_V1 = pd.DataFrame(
    {'date':dates_19,
     'lat':lats_19,
     'lon':lons_19,
     'label':labels_19
    }
)

# Store the Data Fram in a json file
df_fires_19_V1.to_json('fire_data/fire_data_19_V1.json')

# convert machine generated json into human readable format
filename = 'fire_data/fire_data_19_V1.json'
with open(filename) as f:
    fire_data = json.load(f)
    
readable_file = 'fire_data/readable_fire_data_19_V1.json'
with open(readable_file, 'w') as f:
    json.dump(fire_data,f,indent=4)

# Extract fire data from json file
fire_data_19_filename = '/home/code/WS/FungusFinderFireData/usa_fires_2019_archive_M6_90789.json'
with open(fire_data_19_filename) as f:
    all_fire_data_19 = json.load(f)

# Make a list of the date, lon, and latitude
# Filter data to only show fires in Oregon/Washington
dates_19, lats_19, lons_19, labels_19, elevations_19 = [], [], [], [], []
for fire_data_19 in all_fire_data_19:
    date_19 = fire_data_19['acq_date']
    lat_19 = fire_data_19['latitude']
    lon_19 = fire_data_19['longitude']
    if (-115 >= lon_19 >= -120) and (46 >= lat_19 >= 42):
        # get elevations and filter for optimal fungus growth
        try:
            elevation_19 = get_elevation(lat_19,lon_19)
        except ConnectionError:
            elevation_19 = 0
        print(elevation_19)
        dates_19.append(date_19)
        lats_19.append(lat_19)
        lons_19.append(lon_19)

        label_19 = f"Date: {date_19}\
            <br />Lat: {lat_19}\
            <br />Lon: {lon_19}\
            <br />El.: {elevation_19}"
        labels_19.append(label_19)

# Store the data in a Data Frame
df_fires_19_M6 = pd.DataFrame(
    {'date':dates_19,
     'lat':lats_19,
     'lon':lons_19,
     'label':labels_19
    }
)

# Store the Data Fram in a json file
df_fires_19_M6.to_json('fire_data/fire_data_19_M6.json')

# convert machine generated json into human readable format
filename = 'fire_data/fire_data_19_M6.json'
with open(filename) as f:
    fire_data = json.load(f)
    
readable_file = 'fire_data/readable_fire_data_19_M6.json'
with open(readable_file, 'w') as f:
    json.dump(fire_data,f,indent=4)