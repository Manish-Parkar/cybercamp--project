
# import required libraries
import requests
from datetime import datetime

# API key for weather report
apk = '71cd8eceab648caab76f5618f7c935a9'

# enter your desired city name (cina)
cina = input("Enter the city name : ")

# api link to get the weather data
link = "https://api.openweathermap.org/data/2.5/weather?q="+cina+"&appid="+apk

# api link and data in JSON format
api_link = requests.get(link)
api_data = api_link.json()

# assign variables to store and display the weather data
# display longitude and latitude (coordinates) of the location
long = api_data['coord']['lon']
lat = api_data['coord']['lat']

# display country in which the city exist
cy = api_data['sys']['country']

# display current temperature
t = api_data['main']['temp'] - 273.15

# display current weather report
weather_rep = api_data['weather'][-1]['description']

# display current humidity
ht = api_data['main']['humidity']

# display current wind speed
win_spd = api_data['wind']['speed']

# display date and time
dt = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# display full weather report 
print ("-----------------------------------------------------------------")
print ("Weather Report for - {}  || {}".format(cina.upper(), dt))
print ("-----------------------------------------------------------------")
print ("Current Coordinates   : Longitude = {:.3f} and Latitude = {:.3f}".format(long, lat))
print ("Country               :",cy)
print ("Current Temperature   : {:.2f} degree Celsius".format(t))
print ("Current Weather Desc  :",weather_rep)
print ("Current Humidity      :",ht,'%')
print ("Current Wind Speed    :",win_spd ,'kmph')

print("====================================================")


# making a list so that i can print the info to a txt 
wlist = [t,weather_rep,ht,win_spd,dt,long,lat,cy]
print("List = ",wlist)

# using open() buit-in function to write to a text file
# encoding = utf-8 for linux and cp1252 for win
with open("Weather_Report.txt" , mode= 'w' ,encoding= 'cp1252') as f :     
                                      
    f.write("--------------------------------------------------------------- \n ")   
    f.write("Weather Report for - {}  || {}".format(cina.upper(), dt))
    f.write("\n --------------------------------------------------------------- \n")
    f.write("Current Coordinates   : Longitude = {:.3f} and Latitude = {:.3f}\n".format(long, lat))
    f.write("{} {} \n".format("Country                     :",wlist[-1]))
    f.write("Current Temperature  : {:.2f} degree Celsius\n".format(wlist[0]))
    f.write("{} {} \n".format("Current Weather Desc  :" ,wlist[1]))
    f.write("{} {} {} \n".format("Current Humidity      :",wlist[2],"%"))
    f.write("{} {} {} \n".format("Current Wind Speed    :",wlist[3],"kmph"))
    f.write("====================================================")