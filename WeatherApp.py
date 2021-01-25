import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 400

# 2a1be2fd5b32c12d9c929f9cb82100ba
# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (
            name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = '2a1be2fd5b32c12d9c929f9cb82100ba'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params)
    weather = response.json()
    print(weather)
    label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#0099ff", bd=4)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor="n")

entry = tk.Entry(frame)
entry.place(relheight=1, relwidth=0.65)

button = tk.Button(frame, text="Get Weather", fg="black",
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#0099ff", bd=8)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6,
                  relwidth=0.75, anchor="n")

label = tk.Label(lower_frame)
label.place(relheight=1, relwidth=1)

root.mainloop()
