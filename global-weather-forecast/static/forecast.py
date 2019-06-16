import requests
from datetime import date

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def forecast(city):
    apikey = '<YOUR_API_KEY>'
    url = r'http://api.apixu.com/v1/forecast.json?key={}&q={}&days=7'.format(apikey, city)

    response = requests.get(url).json()

    if 'error' in response:
        return 'No data found'

    name = response['location']['name']
    region = response['location']['region']
    country = response['location']['country']

    current = ['Current', str(response['current']['temp_c']) + ' °C',
               response['current']['condition']['text'],
               response['current']['condition']['icon']]

    forecasts = response['forecast']['forecastday']

    forecast_data = list()

    for forecast in forecasts:
        max_temp = forecast['day']['maxtemp_c']
        min_temp = forecast['day']['mintemp_c']
        day = [forecast['date'],
               ['{} °C'.format(max_temp), '{} °C'.format(min_temp)],
               forecast['day']['condition']['text'],
               forecast['day']['condition']['icon']]
        forecast_data.append(day)

    for i in range(len(forecast_data)):
        dt = forecast_data[i][0]
        fdate = date(*list(map(int, dt.split('-'))))
        forecast_data[i][0] = days[fdate.weekday()]

    location = '{}, {}, {}'.format(name, region, country)
    return [location, current, forecast_data]

