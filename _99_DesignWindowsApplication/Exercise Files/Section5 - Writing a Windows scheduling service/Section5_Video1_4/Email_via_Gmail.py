'''
Created on Aug 25, 2016
@author: Burkhard
'''


# NOTE: Might have to be logged into your email account and also have 'Allow access for less secure apps' turned ON
# https://www.google.com/settings/security/lesssecureapps
# from within Settings: https://myaccount.google.com/security?utm_source=OGB#connectedapps


import smtplib
from email.mime.text import MIMEText
from datetime import datetime          
from GMAIL_PWD import GMAIL_PWD     

def send_gmail(msg_file):
    with open(msg_file, mode='rb') as message:              # Open report html file for reading
        msg = MIMEText(message.read(), 'html', 'html')      # Create html message
    
    msg['Subject'] = 'Hourly Weather {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M"))
    msg['From'] = 'PyPro2016@gmail.com'
    msg['To'] = 'another@gmail.com, PyPro2016@gmail.com'     # NO list!       
    
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()       # Extended Hello
    server.starttls()   # Put the SMTP connection in TLS (Transport Layer Security) mode.  
    server.ehlo()       # All SMTP commands that follow will be encrypted.
    server.login('PyPro2016@gmail.com', GMAIL_PWD)
    server.send_message(msg)
    server.close()

#===========================================
if __name__ == '__main__':
    from Get_Weather_Data import get_weather_data
    from Create_Html_file import create_html_report 
    weather_dict, icon = get_weather_data('KLAX')    
    email_file = "Test_Email_File.html"
    create_html_report(weather_dict, icon, email_file)
    send_gmail(email_file)
    
    
    
    