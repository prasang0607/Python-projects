import requests
import json
from bs4 import BeautifulSoup


def get_coordinates(city):
    key = '<YOUR_API_KEY>'
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key={}&query={}".format(key, city)
    # print(url, end='\n')
    raw_data = requests.get(url)
    json_data = json.loads(raw_data.text)

    if(json_data['status'] != 'OK'):
        return "Can't fetch results"

    lat = json_data['results'][0]['geometry']['location']['lat']
    lng = json_data['results'][0]['geometry']['location']['lng']
    address = json_data['results'][0]['formatted_address']
    # print(address)
    return address, lat, lng


def weather_data(city):
    city = city.replace(' ', '_').lower()
    coordinates = get_coordinates(city)

    if type(coordinates) is str:
        return 'No data found.'

    address, lat, lng = coordinates

    try:
        page = requests.get("https://forecast.weather.gov/MapClick.php?lat={}&lon={}".format(lat, lng))
        soup = BeautifulSoup(page.text.replace('<br>', ' '), "lxml")

        items = soup.find_all('div', class_='tombstone-container')

        periods = [item.find('p', class_="period-name").text.strip() for item in items]
        temperatures = [item.find('p', class_="temp").text.strip().split(':')[1].strip() for item in items]
        s_desc = [item.find('p', class_="short-desc").text.strip() for item in items]
    except:
        return 'No data found'

    if len(periods)==0 or len(temperatures)==0 or len(s_desc)==0:
        return 'No data found'

    return address, periods, temperatures, s_desc

