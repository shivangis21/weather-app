import datetime
import json
import urllib.request
import tkinter
from tkinter import *
from tkinter import font

import sys
import os
#from tkinter import PhotoImage

#To convert system time
def time_converter(time):
 converted_time = datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M %p')
 return converted_time


#To build the complete URL
def url_builder(city_name):
  user_api = '79fad313e3e64aefd8e672c67390705d'
  unit = 'metric'
  api = 'http://api.openweathermap.org/data/2.5/weather?q='
  full_api_url = api + str(city_name) + '&mode=json&units=' + unit + '&APPID=' + user_api
  return full_api_url


def data_fetch(full_api_url):
 url = urllib.request.urlopen(full_api_url)
 output = url.read().decode('utf-8')
 raw_api_dict = json.loads(output)
 url.close()
 return raw_api_dict


def data_organizer(raw_api_dict):
 data = dict(
 city=raw_api_dict.get('name'),
 country=raw_api_dict.get('sys').get('country'),
 temp=raw_api_dict.get('main').get('temp'),
 temp_max=raw_api_dict.get('main').get('temp_max'),
 temp_min=raw_api_dict.get('main').get('temp_min'),
 humidity=raw_api_dict.get('main').get('humidity'),
 pressure=raw_api_dict.get('main').get('pressure'),
 sky=raw_api_dict['weather'][0]['main'],
 sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
 sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
 wind=raw_api_dict.get('wind').get('speed'),
 wind_deg=raw_api_dict.get('deg'),
 dt=time_converter(raw_api_dict.get('dt')),
 cloudiness=raw_api_dict.get('clouds').get('all'),
 typeid=raw_api_dict['weather'][0]['id'],
 description=raw_api_dict['weather'][0]['description']
 )
 return data


def data_output(data):
 '''
 m_symbol = '\xb0' + 'C'
 print('---------------------------------------')
 print('Current weather in: {}, {}:'.format(data['city'], data['country']))
 print(data['temp'], m_symbol, data['sky'])
 print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
 print('')
 print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
 print('Humidity: {}'.format(data['humidity']))
 print('Cloud: {}'.format(data['cloudiness']))
 print('Pressure: {}'.format(data['pressure']))
 print('Sunrise at: {}'.format(data['sunrise']))
 print('Sunset at: {}'.format(data['sunset']))
 print('')
 print('Weather ID: {}'.format(data['typeid']))
 print('Last update from the server: {}'.format(data['dt']))
 print('---------------------------------------')
 '''

 global weatherid
 weatherid = ('{}'.format(data['typeid']))
 weathertype = ('{}'.format(data['description']))
 ttemp = (data['temp']) #temperature
 ttma = (data['temp_max']) #max temperature
 ttmi = (data['temp_min']) #min temperature
 hum = (data['humidity'])  #humidity
 pres = (data['pressure']) #pressure
 sk = (data['sky']) #sky
 sr = (data['sunrise']) #sunrise
 ss = (data['sunset']) #sunset
 win = (data['wind']) #wind speed
 wd = (data['wind_deg']) #wind degree
 cloud = (data['cloudiness']) #cloudiness
 d = (data['dt']) #time
 ci = (data['city']) #city
 co = (data['country']) #country

 global root
 root = tkinter.Tk()
 root.geometry('700x500')
 root.title('Weather in:' + " " + str(ci) + ", " + str(co))
 temp = tkinter.Label(root,text=str(ttemp) + "°C",font=("Helvetica", 64, 'bold'))
 temp.grid(row=1,column=0)
 text1 = tkinter.Label(root,text='Max Temp:',font=('bold'))
 tmax = tkinter.Label(root,text=str(ttma) + "°C", font=('bold)'))
 text1.grid(row=0, column=6,sticky=W)
 tmax.grid(row=0, column=7)
 text2 = tkinter.Label(root,text='Min Temp:',font=('bold'))
 tmin = tkinter.Label(root,text=str(ttmi)+"°C",font=('bold'))
 text2.grid(row=0, column=8)
 tmin.grid(row=0, column=9)
 text3 = tkinter.Label(root,justify=RIGHT,text='Humidity:',font=('bold'))
 hu = tkinter.Label(text=str(hum)+ "%",font=('bold'))
 text3.grid(row=1,column=6)
 hu.grid(row=1,column=7)
 text4 = tkinter.Label(root,text='Pressure:',font=('bold'))
 ps = tkinter.Label(root,text=str(pres)+" atm",font=('bold'))
 text4.grid(row=1,column=8)
 ps.grid(row=1,column=9)
 sk = tkinter.Label(root,text=sk,font=('bold'))
 sk.grid(row=0,column=0,sticky=W)
 text5 = tkinter.Label(text='Sunrise')
 srs = tkinter.Label(text=sr)
 text5.grid()
 srs.grid()
 text6 = tkinter.Label(text='Sunset')
 sss = tkinter.Label(text=ss)
 text6.grid()
 sss.grid()
 text7 = tkinter.Label(text='Wind')
 ws = tkinter.Label(text=str(win)+" meter/sec")
 text7.grid()
 ws.grid()
 text8 = tkinter.Label(text='Cloudiness')
 cc = tkinter.Label(text=str(cloud)+ "%")
 text8.grid()
 cc.grid()
 text9 = tkinter.Label(text='Last Updated At:')
 ti = tkinter.Label(text=d)
 text9.grid()
 ti.grid()
 loc= tkinter.Label(text=ci+","+co)
 loc.grid()




if __name__ == '__main__':
  try:
   city_name = input("Enter a city name:")
   data_output(data_organizer(data_fetch(url_builder(city_name))))
  except IOError:
   print('Check your internet connection')
root.mainloop()


