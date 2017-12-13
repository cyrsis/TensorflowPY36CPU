'''
Created on Aug 27, 2016
@author: Burkhard
'''

from Get_Weather_Data import get_weather_data
from Create_Html_file import create_html_report 
from Email_via_Gmail import send_gmail

from collections import OrderedDict
from time import sleep
from pprint import pprint
import schedule

def job():
    pprint(schedule.jobs)
    weather_dict, icon = get_weather_data('KLAX')  
    weather_dict_ordered = OrderedDict(sorted(weather_dict.items())) 
    
    email_file = "Email_File.html"
    create_html_report(weather_dict_ordered, icon, email_file)
    send_gmail(email_file)


# schedule.every().hour.do(job)
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    sleep(1)
    
    
    