from tkinter import *
from tkinter import ttk
from urllib.request import urlopen
from weather_api import weather_list
import datetime
import time
import math
from PIL import Image, ImageTk
import io

# Functios
def to_celsius(kelvin):
    """kelvin to celsius

    Args:
        kelvin (int): number in kelvin

    Returns:
        [int]: number in celsius
    """
    return f"{math.ceil(kelvin - 273.15)}\u00b0"


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

#----------- VARIABLES -----------------
temp = to_celsius(day_dict[0]['temp']['day'])   
feels_temp = to_celsius(day_dict[0]['feels_like']['day'])
wind_speed = day_dict[0]['wind_speed']
clouds = day_dict[0]['clouds']
temp_max = to_celsius(day_dict[0]['temp']['max'])
temp_min = to_celsius(day_dict[0]['temp']['min'])
temp_morn = to_celsius(day_dict[0]['temp']['morn'])
temp_night = to_celsius(day_dict[0]['temp']['night'])
temp_eve = to_celsius(day_dict[0]['temp']['eve'])
weather_description = day_dict[0]['weather'][0]['description']

root = Tk()
root.title('Weather')
root.geometry('400x250')

#----------- Mainframe -----------------
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))



root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

#
city_var = StringVar()
city_var.set('Volgograd')
name_city = ttk.Label(mainframe, textvariable=city_var, font=('monospace', 15))
name_city.grid(column=0, row=0)

#----------- Today -----------------
day_var = StringVar()
day_var.set(today)
date_label = ttk.Label(mainframe, textvariable=day_var)
date_label.grid(column=0, row=1)

# ----------- Frame temperature -----------------
temperature_frame = ttk.Frame(mainframe)
temperature_frame.grid(column=0, row=2)

# ----------- Icons -----------------
get_icon=weather_list[0][0]['weather'][0]['icon']
icon_url = f"http://openweathermap.org/img/wn/{get_icon}@2x.png"
icon_byt = urlopen(icon_url).read()
icon_open = Image.open(io.BytesIO(icon_byt))
icon = ImageTk.PhotoImage(icon_open)
# ----------- Frame icon -----------------
icon_label = ttk.Label(temperature_frame, image=icon)
icon_label.grid(column=0, row=2)

temp_var = StringVar()
temp_var.set(temp)
temp_label = ttk.Label(temperature_frame, text=f"{temp_var.get()}", font=('Arial',  25))
temp_label.grid(column=1, row=2)

# ----------- Frame details -----------------
details_frame = ttk.Frame(mainframe)
details_frame.grid(column=2, row=2)

description_details = ttk.Label(mainframe, text=weather_description)
description_details.grid(column=2, row=2)
temp_feel_like = ttk.Label(mainframe, text=f"feels like {feels_temp}")
temp_feel_like.grid(column=2, row=3)
wind_metr = ttk.Label(mainframe, text=f"{wind_speed} m/s")
wind_metr.grid(column=2, row=4)
clouds_proc = ttk.Label(mainframe, text=f"{clouds}%")
clouds_proc.grid(column=2, row=5)

# wind_var = StringVar()
# wind_var.set(wind_speed)
# wind_label = Label(details_frame, text=f"Wind speed: {wind_var.get()} m/c")
# wind_label.grid(column=1, row=2)

# Clouds, %
# clouds_var = StringVar()
# clouds_var.set(clouds)
# clouds_label = Label(mainframe, text=f"Clouds: {clouds_var.get()}")
# clouds_label.grid(column=0, row=4)


root.mainloop()
