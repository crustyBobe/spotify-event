# For authorization to view user accounts. api-connection.py only works for public data
# This will ask you to open a URL on your browser and accept permission for spotify-event to view data
# After clicking agree the page will show not found, enter the URL of that page into the CLI to get the token
# That token will be passed to other requests and 

import requests
import os
import urllib.parse

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = 'https://127.0.0.1:8000/callback'
SCOPE = 'user-read-private user-top-read user-follow-read'

params = {
    'client_id': CLIENT_ID,
    'response_type': 'code',
    'redirect_uri': REDIRECT_URI,
    'scope': SCOPE
}

auth_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)

print(auth_url)

redirect_response = input('\nPaste the full redirect URL here:\n')

parsed_url = urllib.parse.urlparse(redirect_response)
code = urllib.parse.parse_qs(parsed_url.query).get('code')

code = code[0]

token_url = 'https://accounts.spotify.com/api/token'
payload = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}

response = requests.post(token_url, data=payload)

if response.status_code != 200:
    print("Token request failed:", response.text)

tokens = response.json()
access_token = tokens['access_token']

refresh_token = tokens.get('refresh_token')

headers = {
    'Authorization': f'Bearer {access_token}'
}

print(access_token)
