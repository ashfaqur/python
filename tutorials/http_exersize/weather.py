# module for requesting data from websites
import requests

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
api = input('Enter your Open Weather Map API Key: ')
if not api:
    print('Unfortunately the weather information cannot be retrieved without the API key.'
          '\nYou have to register to "api.openweathermap.org" to get an API key.')
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
print(data)
status = int(data.get(RESPONSE_CODE))

if status != OK_STATUS:
    print('Uh oh! Something went wrong: ' + data.get(ERROR_MESSAGE))
    if status == ERROR_STATUS_API:
        print('It can take a bit of time for the API key to be initialized on Open Weather Map servers.')
    elif status == ERROR_STATUS_CITY:
        print('Please provide a valid city to get its weather information.')
    exit(0)

print(f'The url is {response.url} ')

print(response.json())

temp = round(data.get('main').get('temp'))

print(f'{city} city')
print(f'Current temperature is {temp}\N{DEGREE SIGN}C')
