'''
Created on Aug 7, 2016

@author: Burkh
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
    win.quit()      # win will exist when this function is called
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
fileMenu.add_command(label="Exit", command=_quit)   # command callback
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)
# ---------------------------------------------------------------

# Tab Control / Notebook introduced here ------------------------
tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Tab 1')      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Tab 2')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ---------------------------------------------------------------
    
# We are creating a container frame to hold all other widgets
weather_conditions_frame = ttk.LabelFrame(tab1, text=' Current Weather Conditions ')
# using the tkinter grid layout manager
weather_conditions_frame.grid(column=0, row=0, padx=8, pady=4)

# ---------------------------------------------------------------
# but frame won't be visible until we add widgets to it...
# Adding a Label

## START REFACTORING ---
## COMMENTED OUT AS WE MOVED LABEL TO DIFFERENT PARENT FRAME
# ttk.Label(weather_conditions_frame, text="Location:").grid(column=0, row=0, sticky='W')

# # ---------------------------------------------------------------
# city = tk.StringVar()
# citySelected = ttk.Combobox(weather_conditions_frame, width=12, textvariable=city)
# citySelected['values'] = ('Los Angeles', 'London', 'Rio de Janeiro, Brazil')
# citySelected.grid(column=1, row=0)
# citySelected.current(0)                 # highlight first city
        
# # ---------------------------------------------------------------
# # increase combobox width to longest city
# max_width  = max([len(x)for x in citySelected['values']])
# new_width = max_width
# # new_width = max_width - 4             # adjust per taste of extra spacing
# citySelected.config(width=new_width)
    
# ---------------------------------------------------------------   
#==========================
# ENTRY_WIDTH = max_width + 3             # adjust per taste of alignment
ENTRY_WIDTH = 23
#==========================
## END REFACTORING ---

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

# ****************************************************************
# NOTE: WE REFACTORED THE LABELFRAME VARIABLE TO USE A BETTER NAME
# ****************************************************************
# Add some space around each label
for child in weather_conditions_frame.winfo_children(): 
        child.grid_configure(padx=4, pady=2)    


#########################################################################################
# NOAA section starts here

# first let us move the location/label & combobox out of the weather data
# we create another ttk LabelFrame and position it above the current frame


# We are creating a container frame to hold other widgets
weather_cities_frame = ttk.LabelFrame(tab1, text=' Latest Observation for ')
weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

# ---------------------------------------------------------------
# but frame won't be visible until we add widgets to it...
# Adding a Label
ttk.Label(weather_cities_frame, text="Location:      ").grid(column=0, row=0) # empty space for alignment

# we have to reposition the weather_conditions_frame to the next row below
weather_conditions_frame.grid_configure(column=0, row=1, padx=8, pady=4)

# MOVED FROM LINE 68 to 83 ABOVE:
# ---------------------------------------------------------------
city = tk.StringVar()
# citySelected = ttk.Combobox(weather_conditions_frame, width=12, textvariable=city)    # before
citySelected = ttk.Combobox(weather_cities_frame, width=24, textvariable=city)          # assign different parent
citySelected['values'] = ('Los Angeles', 'London', 'Rio de Janeiro, Brazil')
citySelected.grid(column=1, row=0)
citySelected.current(0)                 # highlight first city
# ---------------------------------------------------------------
for child in weather_cities_frame.winfo_children(): 
        child.grid_configure(padx=6, pady=6)    


#########################################################################################
# NOAA DATA (National Oceanic and Atmospheric Administration) section starts here
# dict data below is a result from web search
weather_data = {
'dewpoint_c': '16.7',
 'dewpoint_f': '62.1',
 'dewpoint_string': '62.1 F (16.7 C)',
 'icon_url_base': 'http://forecast.weather.gov/images/wtf/small/',
 'icon_url_name': 'nsct.png',
 'latitude': '33.93806',
 'location': 'Los Angeles, Los Angeles International Airport, CA',
 'longitude': '-118.38889',
 'ob_url': 'http://www.weather.gov/data/METAR/KLAX.1.txt',
 'observation_time': 'Last Updated on Aug 7 2016, 9:53 pm PDT',
 'observation_time_rfc822': 'Sun, 07 Aug 2016 21:53:00 -0700',
 'pressure_in': '29.81',
 'pressure_mb': '1009.1',
 'pressure_string': '1009.1 mb',
 'relative_humidity': '84',
 'station_id': 'KLAX',
 'suggested_pickup': '15 minutes after the hour',
 'suggested_pickup_period': '60',
 'temp_c': '19.4',
 'temp_f': '67.0',
 'temperature_string': '67.0 F (19.4 C)',
 'two_day_history_url': 'http://www.weather.gov/data/obhistory/KLAX.html',
 'visibility_mi': '9.00',
 'weather': 'Partly Cloudy',
 'wind_degrees': '250',
 'wind_dir': 'West',
 'wind_mph': '6.9',
 'wind_string': 'West at 6.9 MPH (6 KT)'
 }
        
# we want to populate our GUI and we start by using above dict
updated_data = weather_data['observation_time'].replace('Last Updated on ', '')
# next update the Entry widget with this data
updated.set(updated_data)

# we continue to do so for all other entry data
weather.set(weather_data['weather'])
temp.set('{} \xb0F  ({} \xb0C)'.format(weather_data['temp_f'], weather_data['temp_c']))
dew.set('{} \xb0F  ({} \xb0C)'.format(weather_data['dewpoint_f'], weather_data['dewpoint_c']))
rel_humi.set(weather_data['relative_humidity'] + ' %')
wind.set(weather_data['wind_string'])
visi.set(weather_data['visibility_mi'] + ' miles')
msl.set(weather_data['pressure_string'])
alti.set(weather_data['pressure_in'] + ' in Hg')                         
        
#======================
# Start GUI
#======================
win.mainloop()
