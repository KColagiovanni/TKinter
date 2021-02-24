#Import everything from TKinter
from tkinter import *
from PIL import ImageTk, Image
import requests
import json

#Create the main window first, the root widget
root = Tk()

#Change the root window title
root.title("Local AQI")
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
#Define a fixed window size
root.geometry("350x120")

def look_up():

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + user_input.get() + "&distance=2&API_KEY=B2D3B3B6-3A22-4DA8-8BFF-DC514EEEB313")
        api = json.loads(api_request.content)

        city = api[0]['ReportingArea']
        aqi = "\nAQI: " + str(api[0]['AQI'])
        category = " - " + api[0]['Category']['Name']
        number = api[0]['Category']['Number']

        global bg

        if number == 1:
            bg = "#0C0"#Green
        elif number == 2:
            bg = "FFFF00"#Yellow
        elif number == 3:
            bg = "ff9900"#Orange
        elif number == 4:
            bg = "FF0000"#Red
        elif number == 5:
            bg = "990066"#Purple
        else:
            bg = "660000"#Maroon

        root.configure(background = bg)
        api_lbl = Label(root, text = city + aqi + category, background = bg, font = ("Calibri", 16))
        api_lbl.grid(row = 1, column = 0, columnspan = 3)

    except Exception:
        api = "Error..."

zip_lbl = Label(root, text = "Zipcode look up:")
zip_lbl.grid(row = 0, column = 0)
user_input = Entry(root, width = 6)
user_input.grid(row = 0, column = 1)
zip_btn = Button(root, text = "Look up", command = look_up)
zip_btn.grid(row = 0, column = 3)

root.mainloop()