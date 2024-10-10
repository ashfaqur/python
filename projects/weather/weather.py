import os
import requests  # module for requesting data from websites

OPEN_WEATHER_API_KEY_FILE = 'open_weather_map_api_key.txt'

OPEN_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
PARAMETER_CITY = "q"
PARAMETER_APP_ID = "appid"
PARAMETER_UNIT = "units"
PARAMETER_UNIT_VALUE = "metric"

RESPONSE_CODE = 'cod'
OK_STATUS = 200
ERROR_STATUS_API = 401
ERROR_STATUS_CITY = 404
ERROR_MESSAGE = 'message'

print('Welcome to the weather app.')
api_file_path = os.path.join(os.path.expanduser('~'), OPEN_WEATHER_API_KEY_FILE)

try:
    with open(api_file_path) as file:
        api = file.read()
except FileNotFoundError as e:
    api = input('Enter your Open Weather Map API Key: ')

if not api:
    print('Unfortunately the weather information cannot be retrieved without the API key.'
          '\nYou have to register to "api.openweathermap.org" to get an API key.\n'
          'You can also add your key to a file at this location: ' + api_file_path)
    exit(0)

city = input('Enter city name: ')
if not city:
    print('No city given. Exiting.')
    exit(0)

response = requests.get(
    OPEN_WEATHER_URL,
    params={
        PARAMETER_CITY: city,
        PARAMETER_UNIT: PARAMETER_UNIT_VALUE,
        PARAMETER_APP_ID: api
    }
)

data = response.json()
# print(data)
status = int(data.get(RESPONSE_CODE))

if status != OK_STATUS:
    print('Uh oh! Something went wrong: ' + data.get(ERROR_MESSAGE))
    print(f'The url is {response.url} ')
    if status == ERROR_STATUS_API:
        print('It can take a bit of time for the API key to be initialized on Open Weather Map servers.')
    elif status == ERROR_STATUS_CITY:
        print('Please provide a valid city to get its weather information.')
    exit(0)

temp = round(data.get('main').get('temp'))
feels_like = round(data.get('main').get('feels_like'))
weather_description = data.get('weather')[0].get('description')
cloudy_value = data.get('clouds').get('all')
clouds = ''
if 70 < cloudy_value < 90:
    clouds = "It's mostly cloudy"
elif cloudy_value > 90:
    clouds = "Overcast conditions"
wind_value = data.get('wind').get('speed')
wind = ''
if wind_value < 5.5:
    wind = 'Gentle Breeze'
elif 5.5 < wind_value < 10.7:
    wind = 'Fresh Breeze'
else:
    wind = "High Wind"

print('----------------------')
print(f'{city} city')
print('----------------------')
print(f'Current temperature is {temp}\N{DEGREE SIGN}C')
print(f'Feels like {feels_like}\N{DEGREE SIGN}C')
print(f'Weather is {weather_description}')
if clouds:
    print(clouds)
if wind:
    print(wind)
