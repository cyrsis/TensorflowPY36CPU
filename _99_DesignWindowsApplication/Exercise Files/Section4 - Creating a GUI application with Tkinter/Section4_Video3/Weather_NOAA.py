'''
Created on Aug 20, 2016

@author: Burkh
'''

import urllib.request

#TODO: select State, 
#TODO: then filter existing cities
#TODO: then select city


#TODO: Select all data for specified city
# url = 'http://www.weather.gov/xml/current_obs/KSBA.xml'
url_general = 'http://www.weather.gov/xml/current_obs/{}.xml'
city = 'KLAX'
city = 'KSBA'
url = url_general.format(city)

request = urllib.request.urlopen( url )
content = request.read().decode()
# print(content)

#TODO: Retrieve the tags we are interested in
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
    'pressure_in': ''
    }

# Using ElementTree to retrieve specific tags from the xml
import xml.etree.ElementTree as ET
xml_root = ET.fromstring(content)
print('xml_root: {}\n'.format(xml_root.tag))

for data_point in weather_data_tags_dict.keys():
    weather_data_tags_dict[data_point] = xml_root.find(data_point).text

for key, value in weather_data_tags_dict.items():
    print(key, value)















