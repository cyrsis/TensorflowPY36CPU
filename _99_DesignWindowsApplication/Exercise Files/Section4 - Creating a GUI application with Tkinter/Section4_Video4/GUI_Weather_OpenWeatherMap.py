'''
Created on Aug 21, 2016
@author: Burkhard
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
        
#======================
# functions
#======================
# Exit GUI cleanly
def _quit():
    win.quit()      
    win.destroy()
    exit() 

#======================
# procedural code
#======================
# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python Projects")
# ---------------------------------------------------------------
# Creating a Menu Bar
menuBar = Menu()
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)
# ---------------------------------------------------------------

# Tab Control / Notebook 
tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='NOAA')       # Add the tab

tab2 = ttk.Frame(tabControl)                # Add a second tab
tabControl.add(tab2, text='Station IDs')    # Make second tab visible

tab3 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab3, text='Images')     # Make second tab visible

tab4 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab4, text='OpenWeatherMap')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ---------------------------------------------------------------
    
# We are creating a container frame to hold all other widgets
weather_conditions_frame = ttk.LabelFrame(tab1, text=' Current Weather Conditions ')
weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)

#================
ENTRY_WIDTH = 25
#================

# Adding Label & Textbox Entry widgets
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='E')         # <== right-align
updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Weather:").grid(column=0, row=2, sticky='E')               # <== increment row for each
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')                                  # <== increment row for each
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Temperature:").grid(column=0, row=3, sticky='E')
temp = tk.StringVar()
tempEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=temp, state='readonly')
tempEntry.grid(column=1, row=3, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Dewpoint:").grid(column=0, row=4, sticky='E')
dew = tk.StringVar()
dewEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=dew, state='readonly')
dewEntry.grid(column=1, row=4, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='E')
rel_humi = tk.StringVar()
rel_humiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=rel_humi, state='readonly')
rel_humiEntry.grid(column=1, row=5, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Wind:").grid(column=0, row=6, sticky='E')
wind = tk.StringVar()
windEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wind, state='readonly')
windEntry.grid(column=1, row=6, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Visibility:").grid(column=0, row=7, sticky='E')
visi = tk.StringVar()
visiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=visi, state='readonly')
visiEntry.grid(column=1, row=7, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="MSL Pressure:").grid(column=0, row=8, sticky='E')
msl = tk.StringVar()
mslEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=msl, state='readonly')
mslEntry.grid(column=1, row=8, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Altimeter:").grid(column=0, row=9, sticky='E')
alti = tk.StringVar()
altiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=alti, state='readonly')
altiEntry.grid(column=1, row=9, sticky='E')
#---------------------------------------------

# Add some space around each widget
for child in weather_conditions_frame.winfo_children(): 
        child.grid_configure(padx=4, pady=2)    


#########################################################################################
# NOAA (National Oceanic and Atmospheric Administration) section starts here

# We are creating a container frame to hold other widgets
weather_cities_frame = ttk.LabelFrame(tab1, text=' Latest Observation for ')
weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

# ---------------------------------------------------------------
# Adding a Label
ttk.Label(weather_cities_frame, text="Weather Station ID: ").grid(column=0, row=0) # empty space for alignment

# ---------------------------------------------------------------
station_id = tk.StringVar()
station_id_combo = ttk.Combobox(weather_cities_frame, width=6, textvariable=station_id)   
                        # Los Angeles, Denver, New York City       
station_id_combo['values'] = ('KLAX', 'KDEN', 'KNYC')
station_id_combo.grid(column=1, row=0)
station_id_combo.current(0)                 # highlight first city station id

# ---------------------------------------------------------------
# callback function
def _get_station():
    station = station_id_combo.get()
    get_weather_data(station)
    populate_gui_from_dict()

get_weather_btn = ttk.Button(weather_cities_frame,text='Get Weather', command=_get_station).grid(column=2, row=0)

# Station City label
location = tk.StringVar()
ttk.Label(weather_cities_frame, textvariable=location).grid(column=0, row=1, columnspan=3)
# ---------------------------------------------------------------

for child in weather_cities_frame.winfo_children(): 
        child.grid_configure(padx=5, pady=4)    

#########################################################################################
# NOAA DATA directly from live web search

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
#     print(url)
    request = urllib.request.urlopen( url )
    content = request.read().decode()
#     print(content)

    # Using ElementTree to retrieve specific tags from the xml
    import xml.etree.ElementTree as ET
    xml_root = ET.fromstring(content)
#     print('xml_root: {}\n'.format(xml_root.tag))
    
    for data_point in weather_data_tags_dict.keys():
        weather_data_tags_dict[data_point] = xml_root.find(data_point).text
    
#     for key, value in weather_data_tags_dict.items():
#         print(key, value)

# ---------------------------------------------------------------
def populate_gui_from_dict():       
    location.set(weather_data_tags_dict['location'])
    updated.set(weather_data_tags_dict['observation_time'].replace('Last Updated on ', ''))
    weather.set(weather_data_tags_dict['weather'])
    temp.set('{} \xb0F  ({} \xb0C)'.format(weather_data_tags_dict['temp_f'], weather_data_tags_dict['temp_c']))
    dew.set('{} \xb0F  ({} \xb0C)'.format(weather_data_tags_dict['dewpoint_f'], weather_data_tags_dict['dewpoint_c']))
    rel_humi.set(weather_data_tags_dict['relative_humidity'] + ' %')
    wind.set(weather_data_tags_dict['wind_string'])
    visi.set(weather_data_tags_dict['visibility_mi'] + ' miles')
    msl.set(weather_data_tags_dict['pressure_string'])
    alti.set(weather_data_tags_dict['pressure_in'] + ' in Hg')                         


#########################################################################################
# TAB 2
#######
# We are creating a container frame to hold all other widgets
weather_states_frame = ttk.LabelFrame(tab2, text=' Weather Station IDs ')
weather_states_frame.grid(column=0, row=0, padx=8, pady=4)

# ---------------------------------------------------------------
# Adding a Label
ttk.Label(weather_states_frame, text="Select a State: ").grid(column=0, row=0) # empty space for alignment

# ---------------------------------------------------------------
state = tk.StringVar()
state_combo = ttk.Combobox(weather_states_frame, width=5, textvariable=state)         
state_combo['values'] = ('AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI',
                         'ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI',
                         'MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC',
                         'ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
                         'VT','VA','WA','WV','WI','WY'
                        )
state_combo.grid(column=1, row=0)
state_combo.current(0)                 # highlight first

# ---------------------------------------------------------------
# callback function
def _get_cities():
    state = state_combo.get()
    get_city_station_ids(state)

get_weather_btn = ttk.Button(weather_states_frame,text='Get Cities', command=_get_cities).grid(column=2, row=0)

from tkinter import scrolledtext
scr = scrolledtext.ScrolledText(weather_states_frame, width=30, height=17, wrap=tk.WORD)
scr.grid(column=0, row=1, columnspan=3)

# ---------------------------------------------------------------
for child in weather_states_frame.winfo_children(): 
        child.grid_configure(padx=6, pady=6)   


# ---------------------------------------------------------------
def get_city_station_ids(state='ca'):
    url_general = 'http://w1.weather.gov/xml/current_obs/seek.php?state={}&Find=Find'
    state = state.lower()                       # has to be in lower case
    url = url_general.format(state)
    request = urllib.request.urlopen( url )
    content = request.read().decode()
#     print(content)

    parser = WeatherHTMLParser()
    parser.feed(content)
    
    # verify we have as many stations as cities
#     print(len(parser.stations) == len(parser.cities))
    
    scr.delete('1.0', tk.END)  # clear scrolledText widget for next btn click
    
    for idx in range(len(parser.stations)):
        city_station = parser.cities[idx] + ' (' + parser.stations[idx] + ')'
#         print(city_station)
        scr.insert(tk.INSERT, city_station + '\n')
    
#     print(parser.stations)
#     print(parser.cities)



from html.parser import HTMLParser

class WeatherHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stations = []
        self.cities = []
        self.grab_data = False
    
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if "display.php?stid=" in str(attr):
                cleaned_attr= str(attr).replace("('href', 'display.php?stid=", '').replace("')", '')
                self.stations.append(cleaned_attr)
                self.grab_data = True
                
    def handle_data(self, data):
        if self.grab_data:
            self.cities.append(data)
            self.grab_data = False
        
#########################################################################################
# TAB 3
#######
# We are creating a container frame to hold all other widgets
weather_images_frame = ttk.LabelFrame(tab3, text=' Weather Images ')
weather_images_frame.grid(column=0, row=0, padx=8, pady=4)        

# ---------------------------------------------------------------
# requires Pillow (PIL in Python 2.x)
import PIL.Image
import PIL.ImageTk

im = PIL.Image.open("few_clouds.png")
photo = PIL.ImageTk.PhotoImage(im)
ttk.Label(weather_images_frame, image=photo).grid(column=0, row=0) 

im = PIL.Image.open("night_few_clouds.png")
photo1 = PIL.ImageTk.PhotoImage(im)
ttk.Label(weather_images_frame, image=photo1).grid(column=1, row=0) 

im = PIL.Image.open("night_fair.png")
photo2 = PIL.ImageTk.PhotoImage(im)
ttk.Label(weather_images_frame, image=photo2).grid(column=2, row=0) 


#########################################################################################
# TAB 4 OpenWeatherMap
######################

# We are creating a container frame to hold other widgets
open_weather_cities_frame = ttk.LabelFrame(tab4, text=' Latest Observation for ')
open_weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

# Station City label
open_location = tk.StringVar()
ttk.Label(open_weather_cities_frame, textvariable=open_location).grid(column=0, row=1, columnspan=3)

# ---------------------------------------------------------------
# Adding a Label
ttk.Label(open_weather_cities_frame, text="City: ").grid(column=0, row=0) 

# ---------------------------------------------------------------
open_city = tk.StringVar()
open_city_combo = ttk.Combobox(open_weather_cities_frame, width=16, textvariable=open_city)       
open_city_combo['values'] = ('Los Angeles, US', 'London, UK', 'Paris, FR', 'Mumbai, IN', 'Beijing, CN')
open_city_combo.grid(column=1, row=0)
open_city_combo.current(0)                 # highlight first city station id

# ---------------------------------------------------------------
# callback function
def _get_station_open():
    city = open_city_combo.get()
    get_open_weather_data(city)

get_weather_btn = ttk.Button(open_weather_cities_frame,text='Get Weather', command=_get_station_open).grid(column=2, row=0)

# ---------------------------------------------------------------
for child in open_weather_cities_frame.winfo_children(): 
        child.grid_configure(padx=5, pady=2)   

# ---------------------------------------------------------------
# We are creating a container frame to hold all other widgets
open_weather_conditions_frame = ttk.LabelFrame(tab4, text=' Current Weather Conditions ')
open_weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)

#================
ENTRY_WIDTH = 25
#================

# Adding Label & Textbox Entry widgets
#---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='E')         # <== right-align
open_updated = tk.StringVar()
open_updatedEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_updated, state='readonly')
open_updatedEntry.grid(column=1, row=1, sticky='W')
#---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Weather:").grid(column=0, row=2, sticky='E')               # <== increment row for each
open_weather = tk.StringVar()
open_weatherEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_weather, state='readonly')
open_weatherEntry.grid(column=1, row=2, sticky='W')                                  # <== increment row for each
#---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Temperature:").grid(column=0, row=3, sticky='E')
open_temp = tk.StringVar()
open_tempEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_temp, state='readonly')
open_tempEntry.grid(column=1, row=3, sticky='W')
#---------------------------------------------
# ttk.Label(open_weather_conditions_frame, text="Dewpoint:").grid(column=0, row=4, sticky='E')
# dew = tk.StringVar()
# dewEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=dew, state='readonly')
# dewEntry.grid(column=1, row=4, sticky='W')
#---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='E')
open_rel_humi = tk.StringVar()
open_rel_humiEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_rel_humi, state='readonly')
open_rel_humiEntry.grid(column=1, row=5, sticky='W')
#---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Wind:").grid(column=0, row=6, sticky='E')
open_wind = tk.StringVar()
open_windEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_wind, state='readonly')
open_windEntry.grid(column=1, row=6, sticky='W')
#---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Visibility:").grid(column=0, row=7, sticky='E')
open_visi = tk.StringVar()
open_visiEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_visi, state='readonly')
open_visiEntry.grid(column=1, row=7, sticky='W')
#---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Pressure:").grid(column=0, row=8, sticky='E')
open_msl = tk.StringVar()
open_mslEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_msl, state='readonly')
open_mslEntry.grid(column=1, row=8, sticky='W')
#---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Sunrise:").grid(column=0, row=9, sticky='E')
sunrise = tk.StringVar()
sunriseEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=sunrise, state='readonly')
sunriseEntry.grid(column=1, row=9, sticky='E')
#---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Sunset:").grid(column=0, row=10, sticky='E')
sunset = tk.StringVar()
sunsetEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=sunset, state='readonly')
sunsetEntry.grid(column=1, row=10, sticky='E')
#---------------------------------------------

# Add some space around each widget
for child in open_weather_conditions_frame.winfo_children(): 
        child.grid_configure(padx=4, pady=2)    



#########################################################################################
# OpenWeatherMap Data collection

from Section1_Video4.API_key import OWM_API_KEY
from urllib.request import urlopen
import json

def get_open_weather_data(city='London,uk'):
    city = city.replace(' ', '%20')
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, OWM_API_KEY) 
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
    owm_weather = json_data['weather'][0]['description']
    weather_icon = json_data['weather'][0]['icon']
    wind_deg = json_data['wind']['deg']
    wind_speed_meter_sec = json_data['wind']['speed']
        
    def kelvin_to_celsius(temp_k):
        return "{:.1f}".format(temp_k - 273.15)
        
    def kelvin_to_fahrenheit(temp_k):
        return "{:.1f}".format((temp_k - 273.15)* 1.8000 + 32.00)

    from datetime import datetime
    def unix_to_datetime(unix_time):
        return datetime.fromtimestamp(int(unix_time)
        ).strftime('%Y-%m-%d %H:%M:%S')
    
    def meter_to_miles(meter):
        return "{:.2f}".format((meter * 0.00062137))
    
    if visibility_meter is 'N/A':
        visibility_miles = 'N/A'
    else:
        visibility_miles = meter_to_miles(visibility_meter)

    def mps_to_mph(meter_second):
        return "{:.1f}".format((meter_second * (2.23693629)))
    
    # -------------------------------------------------------
    # Update GUI entry widgets with live data
    open_location.set('{}, {}'.format(city_name, city_country))
    
    lastupdate = unix_to_datetime(lastupdate_unix)
    open_updated.set(lastupdate)
    open_weather.set(owm_weather)
    temp_fahr = kelvin_to_fahrenheit(temp_kelvin)
    temp_cels = kelvin_to_celsius(temp_kelvin)
    open_temp.set('{} \xb0F  ({} \xb0C)'.format(temp_fahr, temp_cels))
    open_rel_humi.set('{} %'.format(humidity))
    wind_speed_mph = mps_to_mph(wind_speed_meter_sec)
    open_wind.set('{} degrees at {} MPH'.format(wind_deg, wind_speed_mph))
    open_visi.set('{} miles'.format(visibility_miles))
    open_msl.set('{} hPa'.format(pressure))
    sunrise_dt = unix_to_datetime(sunrise_unix)
    sunrise.set(sunrise_dt)
    sunset_dt = unix_to_datetime(sunset_unix)
    sunset.set(sunset_dt)
    
    print(weather_icon)
    url_icon = "http://openweathermap.org/img/w/{}.png".format(weather_icon)
    ico = urlopen(url_icon)
    open_im = PIL.Image.open(ico)
    open_photo = PIL.ImageTk.PhotoImage(open_im)
    ttk.Label(open_weather_cities_frame, image=open_photo).grid(column=0, row=1) 
    win.update()        # required or we won't see the icon

#======================
# Start GUI
#======================
# get_weather_data()
# populate_gui_from_dict()
win.mainloop()
