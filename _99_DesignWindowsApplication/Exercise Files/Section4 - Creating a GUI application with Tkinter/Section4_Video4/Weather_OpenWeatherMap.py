'''
Created on Aug 21, 2016
@author: Burkhard
'''

from Section1_Video4.API_key import OWM_API_KEY
from urllib.request import urlopen
import json

url = "http://api.openweathermap.org/data/2.5/weather?q=Los%20Angeles,us&appid={}".format(OWM_API_KEY) 
response = urlopen(url)
data = response.read().decode()
json_data = json.loads(data)

from pprint import pprint
pprint(json_data)

lat_long = json_data['coord']
lastupdate_unix = json_data['dt']
city_id = json_data['id']
humidity = json_data['main']['humidity']
pressure = json_data['main']['pressure']
temp_kelvin = json_data['main']['temp']
city_name = json_data['name']
city_country = json_data['sys']['country']
sunrise_unix = json_data['sys']['sunrise']
sunset_unix = json_data['sys']['sunset']
try: visibility_meter = json_data['visibility']
except: visibility_meter = 'N/A'
weather = json_data['weather'][0]['description']
weather_icon = json_data['weather'][0]['icon']
wind_deg = json_data['wind']['deg']
wind_speed_meter_sec = json_data['wind']['speed']


def kelvin_to_celsius(temp_k):
    return "{:.2f}".format(temp_k - 273.15)
    

def kelvin_to_fahrenheit(temp_k):
    return "{:.2f}".format((temp_k - 273.15)* 1.8000 + 32.00)

print(kelvin_to_fahrenheit(temp_kelvin))    
print(kelvin_to_celsius(temp_kelvin))    


from datetime import datetime
def unix_to_datetime(unix_time):
    return datetime.fromtimestamp(int(unix_time)
    ).strftime('%Y-%m-%d %H:%M:%S')
print(unix_to_datetime(lastupdate_unix))


def meter_to_miles(meter):
    return "{:.1f}".format((meter * 0.00062137))

if visibility_meter is 'N/A':
    visibility_miles = 'N/A'
else:
    visibility_miles = meter_to_miles(visibility_meter)
print(visibility_miles)


def mps_to_mph(meter_second):
    return "{:.1f}".format((meter_second * (2.23693629)))

print(mps_to_mph(3.1))
 
