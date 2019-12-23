import json
import pandas as pd
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from get_elevation import get_elevation

from pandas import DataFrame


def fire_data_filter(data_source, data_file_in, data_file_out):
    """ Takes a NASA-FIRMS data file, filters the data to only
        show fires in western Oregon and Washington.  Also
        retrieves the elevation from the lat/long coordinates
    """
    # Extract fire data from json file
    with open(data_file_in) as f:
        all_fire_data = json.load(f)

    # Make a list of the date, lon, and latitude
    # Filter data to only show fires in Oregon/Washington
    dates, lats, lons, labels, elevations = [], [], [], [], []
    for fire_data in all_fire_data:
        date = fire_data['acq_date']
        lat = fire_data['latitude']
        lon = fire_data['longitude']
        if (-120 >= lon >= -125) and (47 >= lat >= 42):
            # get elevations and filter for optimal fungus growth
            try:
                elevation = get_elevation(lat,lon)
            except ConnectionError:
                elevation = 0
            print(elevation)
            dates.append(date)
            lats.append(lat)
            lons.append(lon)
            elevations.append(elevation)

            label = f"Date: {date}\
                <br />Lat: {lat}\
                <br />Lon: {lon}\
                <br />El.: {elevation}\
                <br />Data Source: {data_source}"
            labels.append(label)

    # Store the data in a Data Frame
    df_fires = pd.DataFrame(
        {'date':dates,
         'lat':lats,
         'lon':lons,
         'elevation':elevations,
         'label':labels
        }
    )

    # Store the Data Fram in a json file
    df_fires.to_json(data_file_out)

    ## convert machine generated json into human readable format
    #filename = 'fire_data/fire_data_18_V1.json'
    #with open(filename) as f:
    #    fire_data = json.load(f)

    #readable_file = 'fire_data/readable_fire_data_18_V1.json'
    #with open(readable_file, 'w') as f:
    #    json.dump(fire_data,f,indent=4)

##-------------------------
## 2019 USA Fire Data 
## ------------------------
#data_source_19_v1 = 'VIIRS'
#fd_file_19_v1 = '/home/code/WS/FungusFinderFireData/usa_fires_2019_archive_V1.json'
#filtered_fd_file_19_v1 = ('fire_data/filtered_fire_data_19_V1.json')    
#
#data_source_19_m6 = 'MODIS C6'
#fd_file_19_m6 = '/home/code/WS/FungusFinderFireData/usa_fires_2019_archive_M6.json'
#filtered_fd_file_19_m6 = ('fire_data/filtered_fire_data_19_M6.json')
#
## Filter the Data, Get Elevations, And store to Json File
#fire_data_filter(data_source_19_v1, fd_file_19_v1, filtered_fd_file_19_v1)
#fire_data_filter(data_source_19_m6, fd_file_19_m6, filtered_fd_file_19_m6)
#
##-------------------------
## 2018 USA Fire Data 
## ------------------------
#data_source_18_v1 = 'VIIRS'
#fd_file_18_v1 = '/home/code/WS/FungusFinderFireData/usa_fires_2018_archive_V1.json'
#filtered_fd_file_18_v1 = ('fire_data/filtered_fire_data_18_V1.json')    
#
#data_source_18_m6 = 'MODIS C6'
#fd_file_18_m6 = '/home/code/WS/FungusFinderFireData/usa_fires_2018_archive_M6.json'
#filtered_fd_file_18_m6 = ('fire_data/filtered_fire_data_18_M6.json')
#
## Filter the Data, Get Elevations, And store to Json File
#fire_data_filter(data_source_18_v1, fd_file_18_v1, filtered_fd_file_18_v1)
#fire_data_filter(data_source_18_m6, fd_file_18_m6, filtered_fd_file_18_m6)
#
##-------------------------
## 2017 USA Fire Data 
## ------------------------
#data_source_17_v1 = 'VIIRS'
#fd_file_17_v1 = '/home/code/WS/FungusFinderFireData/usa_fires_2017_archive_V1.json'
#filtered_fd_file_17_v1 = ('fire_data/filtered_fire_data_17_V1.json')    
#
#data_source_17_m6 = 'MODIS C6'
#fd_file_17_m6 = '/home/code/WS/FungusFinderFireData/usa_fires_2017_archive_M6.json'
#filtered_fd_file_17_m6 = ('fire_data/filtered_fire_data_17_M6.json')
#
## Filter the Data, Get Elevations, And store to Json File
#fire_data_filter(data_source_17_v1, fd_file_17_v1, filtered_fd_file_17_v1)
#fire_data_filter(data_source_17_m6, fd_file_17_m6, filtered_fd_file_17_m6)

#-------------------------
# 2016 USA Fire Data 
# ------------------------
data_source_16_v1 = 'VIIRS'
fd_file_16_v1 = '/home/code/WS/FungusFinderFireData/usa_fires_2016_archive_V1.json'
filtered_fd_file_16_v1 = ('fire_data/filtered_fire_data_16_V1.json')    

data_source_16_m6 = 'MODIS C6'
fd_file_16_m6 = '/home/code/WS/FungusFinderFireData/usa_fires_2016_archive_M6.json'
filtered_fd_file_16_m6 = ('fire_data/filtered_fire_data_16_M6.json')

# Filter the Data, Get Elevations, And store to Json File
fire_data_filter(data_source_16_v1, fd_file_16_v1, filtered_fd_file_16_v1)
fire_data_filter(data_source_16_m6, fd_file_16_m6, filtered_fd_file_16_m6)