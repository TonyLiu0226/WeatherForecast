import bs4
from bs4 import BeautifulSoup
import requests
from datetime import datetime

def forecast(city):

    try:
        url = "https://www.google.com/search?q="+"weather"+city

        data = requests.get(url).content
        b4 = BeautifulSoup(data, 'lxml')

        #prints out the current temperature
        gay = b4.find_all('div')
        if len(gay) == 0:
            raise Exception("Invalid city entered")

        currentTemp = b4.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        currentTime = b4.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        forecast = b4.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).text
        print("The weather for " + city + ": " + currentTime + ". Temperature: " +currentTemp)
        print("Your 3 day forecast is: " +forecast)
        #prints out the current weather condition
        print(gay)
    
        #prints out the weather and temperature for today


        #prints out the weather and temperature for tomorrow

    except Exception as e:
        print("Invalid city name entered")
        print(e)

city = input('Enter a city name: ')
forecast(city)
