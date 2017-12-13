'''
Created on Aug 20, 2016

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
tabControl.add(tab1, text='Tab 1')      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Tab 2')      # Make second tab visible

tab3 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab3, text='Tab 3')      # Make second tab visible

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
    print(url)
    request = urllib.request.urlopen( url )
    content = request.read().decode()
#     print(content)

    # Using ElementTree to retrieve specific tags from the xml
    import xml.etree.ElementTree as ET
    xml_root = ET.fromstring(content)
    print('xml_root: {}\n'.format(xml_root.tag))
    
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
    print(len(parser.stations) == len(parser.cities))
    
    scr.delete('1.0', tk.END)  # clear scrolledText widget for next btn click
    
    for idx in range(len(parser.stations)):
        city_station = parser.cities[idx] + ' (' + parser.stations[idx] + ')'
        print(city_station)
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


#======================
# Start GUI
#======================
# get_weather_data()
# populate_gui_from_dict()
win.mainloop()
