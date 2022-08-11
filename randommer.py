import requests


API_KEY = '2d794c6f46094ceb96bd719c1c26c984'
URL = 'https://randommer.io/api/Card/Types'


headers = {
    'X-Api-Key': API_KEY
}

r = requests.get(url=URL, headers=headers)
print(r.json())