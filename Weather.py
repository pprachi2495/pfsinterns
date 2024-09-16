# -*- coding: latin-1 -*-
import tkinter as tk
import requests
import time

def getWeather(event=None):  
    city = textfield.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fbdaaad74b17f4cdc51a17346a272465"
    json_data = requests.get(api).json()

    if json_data.get('cod') != 200:
        final_info = "City not found"
        final_data = ""
    else:
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = f"{condition}\n{temp}°C"
        final_data = (f"Max Temp: {max_temp}°C\n"
                      f"Min Temp: {min_temp}°C\n"
                      f"Pressure: {pressure} hPa\n"
                      f"Humidity: {humidity}%\n"
                      f"Wind Speed: {wind} m/s\n"
                      f"Sunrise: {sunrise}\n"
                      f"Sunset: {sunset}")

    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather Application")
canvas.configure(bg='sky blue')


f = ("poppins", 15, "bold")
t = ("poppins", 20, "bold")


heading_label = tk.Label(canvas, text="Weather Forecast App", font=("poppins", 30, "bold"), bg='sky blue')
heading_label.pack(pady=10)


prompt_label = tk.Label(canvas, text="Enter the City Name :" , font=f, bg='sky blue')
prompt_label.pack(pady=10)


textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)  

submit_button = tk.Button(canvas, text="Get Weather", command=getWeather)
submit_button.pack(pady=10)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()

