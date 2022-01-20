from tkinter import *
from weather_api import weather_list
import datetime
import math

# Functios
def to_celsius(kelvin):
    """kelvin to celsius

    Args:
        kelvin (int): number in kelvin

    Returns:
        [int]: number in celsius
    """
    return math.ceil(kelvin - 273.15) 

def get_date(weather_list):
    pass

def get_time(weather_list, days=0):
    for d in weather_list[days]:
        day = d['dt']
        
    today = datetime.datetime.fromtimestamp(day)
    return today.strftime('%d.%m.%Y')

day_dict = weather_list[0]

today = get_time(weather_list)

temp = to_celsius(day_dict[0]['temp']['day'])   
feels_temp = to_celsius(day_dict[0]['feels_like']['day'])
wind_speed = day_dict[0]['wind_speed']
clouds = day_dict[0]['clouds']
temp_max = to_celsius(day_dict[0]['temp']['max'])
temp_min = to_celsius(day_dict[0]['temp']['min'])
temp_morn = to_celsius(day_dict[0]['temp']['morn'])
temp_night = to_celsius(day_dict[0]['temp']['night'])
temp_eve = to_celsius(day_dict[0]['temp']['eve'])

window = Tk()
window.title('Weather')
window.geometry('400x250')

name_city = Label(window, text='Volgograd', font=('monospace', 15))
name_city.grid(column=0, row=0)

date_label = Label(window, text=today)
date_label.grid(column=0, row=1)

temp_label = Label(window, text=f"Temperature: {temp} C", justify=LEFT)
temp_label.grid(column=0, row=2)

wind_label = Label(window, text=f"Wind speed: {wind_speed} m/c", justify=LEFT)
wind_label.grid(column=0, row=3)

clouds_label = Label(window, text=f"Clouds: {clouds}", justify=LEFT)
clouds_label.grid(column=0, row=4)



window.mainloop()
