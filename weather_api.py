import requests

city = 'Volgograd,ru'

def city_forecast(lat=48.719391, lon=44.501839):
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=48.719391&lon=44.501839&exclude=current,minutely,hourly,alerts&appid=7f2adad08b9a9e81b4072e7de76eabd1")
    
    return response.json()

date = city_forecast(city)

def write_in_list(data):
    """this is function records the required params.
    Args: data: JSON list
    Returns: list of new params
    """
    weather_list = []
    for d in range(len(data['daily'])):
        weather_list.append([{
            'dt': data['daily'][d]['dt'],
            'temp': data['daily'][d]['temp'],
            'feels_like': data['daily'][d]["feels_like"],
            'wind_speed': data['daily'][d]["wind_speed"],
            'clouds': data['daily'][d]['clouds']
        }])   

    return weather_list

weather_list = write_in_list(date)