from tkinter import *
import requests

api_key = "95a339616fdb83a0c7efb7d776ce1d42"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather_data(location):

    url = base_url + "q=" + location + "&appid=" + api_key

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error retrieving weather data: ", response.status_code)

def display_weather_data(data):
    temp = data['main']['temp']
    description = data['weather'][0]['discription']
    wind_speed = data['wind']['speed']
    wind_direction = data['wind']['deg']

    if wind_direction >= 337.5 or wind_direction < 22.5:
       wind_direction = "N"
    elif wind_direction >= 22.5 and wind_direction < 67.5:
       wind_direction = "NE"
    elif wind_direction >= 67.5 and wind_direction < 112.5:
       wind_direction = "E"
    elif wind_direction >= 112.5 and wind_direction < 157.5:
       wind_direction = "SE"
    elif wind_direction >= 157.5 and wind_direction < 202.5:
       wind_direction = "S"
    elif wind_direction >= 202.5 and wind_direction < 247.5:
       wind_direction = "SW"
    elif wind_direction >= 247.5 and wind_direction < 292.5:
       wind_direction = "W"
    elif wind_direction >= 292.5 and wind_direction < 337.5:
       wind_direction = "NW"

    weather_string = f"Temprature: {temp: 1f}C\nConditions: {description}\nWind speed: {wind_speed}m\s\nWind direction: {wind_direction}"

    weather_label.config(Text=weather_string)

def get_weather():

    location = location_entry.get()
    weather_data = get_weather_data(location)

    if weather_data:
        display_weather_data(weather_data)
    else:
        weather_label.config(text="Error retrieving weather data")

root = Tk()
root.title("Weather Proggram")

lcoation_label = Label(root, text= "Enter location: ")

location_entry = Entry(root)

get_weather_button = Button(root, text="get weather", command=get_weather)

weather_label = Label(root, text="", justify="left")

lcoation_label.pack()
location_entry.pack()
get_weather_button.pack()
weather_label.pack()

root.mainloop()    