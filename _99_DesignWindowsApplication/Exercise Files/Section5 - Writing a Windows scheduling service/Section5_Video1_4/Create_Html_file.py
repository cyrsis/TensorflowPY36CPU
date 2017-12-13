'''
Created on Aug 27, 2016
@author: Burkhard
'''

from datetime import datetime

def create_html_report(data_dict, icon_url, html_file):
    
    alt_var = data_dict['weather']
   
    with open(html_file, mode='w') as outfile:
        outfile.write( '\t<tr><td align="center">' + datetime.now()
                       .strftime("%Y-%m-%d %H:%M:%S") +'</td></tr><br>\n' )
        outfile.write( '<img alt={} src={}>'.format(alt_var, icon_url))
        outfile.write( '<br><span style="color:blue"><b>\tWeather Data:</b>\n' )
        outfile.write( '<br>')    
            
        outfile.write( '<html><table border=1>\n' )
        #--------------------------------------------
        for key, value in data_dict.items():
            outfile.write( '<tr><td><b><span style="color:black">{:s}</b></td><td align="left"> \
                <span style="color:blue"><b>{:s}</b></td></tr>\n'.format(key, value))
        #--------------------------------------------
        outfile.write( '</table></html>\n' )

#===========================================
if __name__ == '__main__':
    from Get_Weather_Data import get_weather_data
    weather_dict, icon = get_weather_data('KLAX')
    create_html_report(weather_dict, icon, "Test_Email_File.html")
    
                