import requests
import os
from requests.auth import HTTPBasicAuth

client_id = os.environ.get(CLIENT_ID)
secret_key = os.environ.get(SECRET_KEY)
username = os.environ.get(USERNAME)
password = os.environ.get(PASSWORD)
base_url = 'https://www.reddit.com/'
api_url = 'https://oauth.reddit.com'

auth = requests.auth.HTTPBasicAuth(client_id, secret_key)

data = {'grant_type': 'password', 'username': username, 'password': password}

headers = {'User-Agent': 'AFLLiveComments/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

res = requests.get(api_url + 'live/thread', headers=headers)

print(res.json())

# if __name__ == '__main__':
#     print()
