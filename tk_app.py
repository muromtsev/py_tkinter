from tkinter import *
from tkinter import ttk
from weather_api import weather_list
import datetime
import time
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

def get_string_date(weather_list, days=0):
    names_of_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    names_of_months = ['Junuary', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    result = ''           
    t = time.localtime()
    count = 1
    for d in weather_list[days]:
        day = d['dt']

    today = datetime.datetime.fromtimestamp(day)

    current_day = today.strftime('%d')
    current_month = today.strftime('%m')

    if days == 0:
        return f"{names_of_days[t[6]]}, {t[2]} {names_of_months[t[1]]}, {t[3]}:{t[4]}"    
    else:
        return today.strftime('%d.%m.%Y')

day_dict = weather_list[0]

today = get_string_date(weather_list)
#-----------variables-----------------
temp = to_celsius(day_dict[0]['temp']['day'])   
feels_temp = to_celsius(day_dict[0]['feels_like']['day'])
wind_speed = day_dict[0]['wind_speed']
clouds = day_dict[0]['clouds']
temp_max = to_celsius(day_dict[0]['temp']['max'])
temp_min = to_celsius(day_dict[0]['temp']['min'])
temp_morn = to_celsius(day_dict[0]['temp']['morn'])
temp_night = to_celsius(day_dict[0]['temp']['night'])
temp_eve = to_celsius(day_dict[0]['temp']['eve'])

root = Tk()
root.title('Weather')
root.geometry('400x250')

# Mainframe
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# City
city_var = StringVar()
city_var.set('Volgograd')
name_city = Label(mainframe, textvariable=city_var, font=('monospace', 15), background='pink')
name_city.grid(column=0, row=0)

# Today
day_var = StringVar()
day_var.set(today)
date_label = Label(mainframe, textvariable=day_var)
date_label.grid(column=0, row=1)

# Temperature today
temp_var = IntVar()
temp_var.set(temp)
temp_label = Label(mainframe, text=f"{temp_var.get()}\u00b0")
temp_label.grid(column=0, row=2)

# Wind, m/s
wind_var = IntVar()
wind_var.set(wind_speed)
wind_label = Label(mainframe, text=f"Wind speed: {wind_var.get()} m/c")
wind_label.grid(column=0, row=3)

# Clouds, %
clouds_var = IntVar()
clouds_var.set(clouds)
clouds_label = Label(mainframe, text=f"Clouds: {clouds_var.get()}")
clouds_label.grid(column=0, row=4)


root.mainloop()
