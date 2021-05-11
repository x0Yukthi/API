import tkinter as tk
import time
import requests

def getWeather(canvas):
    city = textfield.get()
    #for appid give the api key
    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="
    json_data = requests.get(api).json()
    cond = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    speed = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 21600))
    
    final_info = cond + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(speed) + "\n" + "Sunrise: " + sunrise + " AM"+"\n" + "Sunset: " + sunset+" PM"
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry('600x700')
canvas.title("Weather Report")
canvas.configure(bg='#505e54')

f =('Courier New',18,"bold")
t =('Comic Sans MS',35,"bold")

textfield = tk.Entry(canvas,fg ='#505e54',bg = "#ccdbd0" ,font=t)
textfield.pack(pady = 25)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, fg = "#ccdbd0",
		 bg = "#505e54", font = t)
label1.pack()

label2 = tk.Label(canvas,fg = "#ccdbd0",
		 bg = "#505e54", font = f)
label2.pack()

canvas.mainloop()
