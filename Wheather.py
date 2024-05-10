import tkinter as tk
from tkinter import messagebox, font
import requests

def get_weather(city):
    try:
        api_key = "enter your API key"
        base_url = "enter the url"
        complete_url = f"{base_url}q={city}&appid={api_key}"
        response = requests.get(complete_url)
        weather_data = response.json()

        if weather_data.get("cod") == 200:
            main_data = weather_data["main"]
            temperature = main_data["temp"] - 273.15  # Convert Kelvin to Celsius
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            weather_description = weather_data["weather"][0]["description"]
            result = (f"Temperature: {temperature:.2f}°C\n"
                      f"Pressure: {pressure} hPa\n"
                      f"Humidity: {humidity}%\n"
                      f"Description: {weather_description.capitalize()}")
        else:
            result = "City Not Found"
    except Exception as e:
        result = f"Error: {str(e)}"

    return result

def show_weather():
    city = city_name_entry.get()
    weather = get_weather(city)
    weather_result_label.config(text=weather)

# Creating the main window
root = tk.Tk()
root.title("Weather App")
root.geometry('400x300') 
root.config(bg='light blue')  

# Font configuration
font_style = font.Font(family="Lucida Grande", size=12)

# Adding widgets
city_name_label = tk.Label(root, text="Enter city name:", bg='light blue', fg='dark blue', font="50")
city_name_label.pack(pady=10,padx=50)

city_name_entry = tk.Entry(root, font=font_style)
city_name_entry.pack(pady=5,padx=10)

search_button = tk.Button(root, text="Get Weather", command=show_weather, font=font_style, bg='blue', fg='white')
search_button.pack(pady=10)

weather_result_label = tk.Label(root, text="", bg='light blue', fg='dark green', font=font_style)
weather_result_label.pack(pady=10)

# Start the GUI
root.mainloop()
