import tkinter, requests
from tkinter import BOTH, IntVar
from PIL import ImageTk, Image
from io import BytesIO
root = tkinter.Tk()
root.title('Weathe App')
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0,0)

#define colors and fonts
sky_color = "#9FC2CC"
grass_color = "#20BF55"
input_color = "#50FFB1"
output_color = "#81F7E5"
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)

#define functions
def search():
    global response

    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "a21df2a0766cf894f487aedc536bc0e4"
    if search_method.get() == 1:
        querystring = {"q" : city_entry.get(), "appid":api_key, "units": "metric"}
    elif search_method.get() == 2:
        querystring = {"q" : city_entry.get(), "appid":api_key, "units":"metric"}

    response = requests.request("GET", url, params=querystring)
    response = response.json()

    get_weather()
    icon_image()

def get_weather():
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])        
    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']
    temp = str(response['main']['temp'])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    pressure = str(response['main']['pressure'])
    humidity = str(response['main']['humidity'])

    #update output labels
    city_info_label.config(text=city_name + "(" + city_lat + "," + city_lon + ")", font=large_font, bg=output_color)
    weather_label.config(text="Weather is::  " + main_weather + " , " + description, font=small_font, bg=output_color)
    temp_label.config(text="Temparatur is :: " + temp + " C", font=small_font, bg=output_color)
    temp_max_label.config(text="Maximum Temparature is :: " + temp_max + " C", font=small_font, bg=output_color)
    temp_min_label.config(text="Minimum Temparature is :: " + temp_min + " C", font=small_font, bg=output_color)
    humidity_label.config(text="Humidity is :: " + humidity, font=small_font, bg=output_color)
    feels_label.config(text="Feels like :: " + feels_like + " C", font=small_font, bg=output_color)
    pressure_label.config(text="Pressure is :: " + pressure + " Pa", font=small_font, bg=output_color)

def icon_image():
    global img
    icon_id = response['weather'][0]['icon']
    # print(icon_id)
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
    icon_response = requests.get(url, stream=True)
    # print(icon_response)

    img_data = icon_response.content
    # print(img_data)
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    # print(img)
    photo_label.config(image=img)



#define layout
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)
output_frame = tkinter.Frame(sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.Frame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)
#output frame layout
city_info_label = tkinter.Label(output_frame, bg=output_color)
weather_label = tkinter.Label(output_frame, bg=output_color)
temp_label = tkinter.Label(output_frame, bg=output_color)
feels_label = tkinter.Label(output_frame, bg=output_color)
temp_min_label = tkinter.Label(output_frame, bg=output_color)
temp_max_label = tkinter.Label(output_frame, bg=output_color)
humidity_label = tkinter.Label(output_frame, bg=output_color)
pressure_label = tkinter.Label(output_frame, bg=output_color)
photo_label = tkinter.Label(output_frame, bg=output_color)
city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
pressure_label.pack()
photo_label.pack(pady=8)

#input frame layout
city_entry = tkinter.Entry(input_frame, width=20, font=large_font)
submit_button = tkinter.Button(input_frame, text="Submit", bg=input_color, font=large_font, command=search)
search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text="Submit Search City", variable=search_method, value=1, bg=input_color, font=small_font)
search_zip = tkinter.Radiobutton(input_frame, text="Submit by ZIP Code", variable=search_method, value=2, bg=input_color, font=small_font)
city_entry.grid(row=0, column=0, padx=10, pady=(10, 0))
submit_button.grid(row=0, column=1, padx=10, pady=(10, 0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, pady=2)

root.mainloop()