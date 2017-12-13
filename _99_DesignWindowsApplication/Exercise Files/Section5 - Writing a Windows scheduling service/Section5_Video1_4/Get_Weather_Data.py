'''
Created on Aug 27, 2016
@author: Burkhard
'''


#################################################################
# NOAA weather data from live web search

#Retrieve the tags we are interested in
weather_data_tags_dict = {
    'observation_time': '',
    'weather': '',
    'temp_f':  '',
    'temp_c':  '',
    'dewpoint_f': '',
    'dewpoint_c': '',
    'relative_humidity': '',
    'wind_string':   '',
    'visibility_mi': '',
    'pressure_string': '',
    'pressure_in': '',
    'location': ''
    }

# ---------------------------------------------------------------
import urllib.request

def get_weather_data(station_id='KLAX'):
    url_general = 'http://www.weather.gov/xml/current_obs/{}.xml'
    url = url_general.format(station_id)
    request = urllib.request.urlopen( url )
    content = request.read().decode()

    # Using ElementTree to retrieve specific tags from the xml
    import xml.etree.ElementTree as ET
    xml_root = ET.fromstring(content)

    for data_point in weather_data_tags_dict.keys():
        weather_data_tags_dict[data_point] = xml_root.find(data_point).text

    icon_url_base = xml_root.find('icon_url_base' ).text
    icon_url_name = xml_root.find('icon_url_name' ).text
    icon_url = icon_url_base + icon_url_name
    
    return weather_data_tags_dict, icon_url


#===========================================
if __name__ == '__main__':
    weather_dict, icon = get_weather_data()
    from pprint import pprint
    pprint(weather_dict)
    print(icon)