import requests

GOOGLE_URL = 'http://google.com'

# response = requests.get(GOOGLE_URL)
#
# print(f'Your response to {GOOGLE_URL} came back with status {response.status_code}')
#
# print(f'Response text from {GOOGLE_URL}:')
# print(response.text)

DAD_JOKE_URL = 'https://icanhazdadjoke.com/search'

response = requests.get(
    DAD_JOKE_URL,
    headers={"Accept": "application/json"},
    params={'term': 'cat', 'limit':1}
)

data = response.json()

print(data.get('results'))
