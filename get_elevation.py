
import requests
import urllib
import json
import simplejson

def get_elevation(lat,lon,units='Feet'):
    """
    Returns elevation based on lat and long coordinates.
    Can Select 'Meters' or 'Feet'
    """
    # Make an API call and store the response
    try:
        url = r'https://nationalmap.gov/epqs/pqs.php?'
        # Define Query Parameters
        params = {
            'output':'json',
            'x':lon,
            'y':lat,
            'units':units #Can be Meters
        }
        r = requests.get((url + urllib.parse.urlencode(params)))

        # Store API response in a variable
        elevation = r.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation']
        # one approach is to use pandas json functionality:
        #elevation = pd.io.json.json_normalize(r, 'results')['elevation'].values[0]
        #print(elevation)
    except (requests.exceptions.ConnectionError, simplejson.errors.JSONDecodeError):
        elevation = 0
    
    return elevation 