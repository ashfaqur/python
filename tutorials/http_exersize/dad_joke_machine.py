import random

import requests

import dad_joke_title

DAD_JOKE_SEARCH_URL = 'https://icanhazdadjoke.com/search'
RESPONSE_STATUS = 'status'
RESPONSE_TOTAL_JOKES = 'total_jokes'
RESPONSE_RESULTS = 'results'
RESPONSE_JOKE_KEY = 'joke'

dad_joke_title.show()

print('Ahh yes! You have come to the right place.')
topic = input('About which topic do you want to hear a joke about?\n')

response = requests.get(
    DAD_JOKE_SEARCH_URL,
    headers={'Accept': 'application/json'},
    params={'term': topic}
)

data = response.json()

status = data.get(RESPONSE_STATUS)
if status != 200:
    print('Uh oh! Something went wrong with requesting a joke.')
    print(data)

total_jokes = data.get(RESPONSE_TOTAL_JOKES)

if total_jokes:
    if total_jokes > 1:
        print(f'Nice! I got {total_jokes} jokes about "{topic}". Here is one:')
    else:
        print(f'Nice! I got joke about "{topic}". Here it is:')
else:
    print(f'Uh oh! I got no jokes about "{topic}"')
    exit(0)

all_jokes = data.get(RESPONSE_RESULTS)

item = random.choice(all_jokes)
the_joke = item.get(RESPONSE_JOKE_KEY)
print(the_joke)
