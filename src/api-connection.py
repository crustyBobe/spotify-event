import requests
import os
import json

from auth import headers

# Set auth credentials
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

# Set users's ID. TODO: Get ID from user input and verify
USER_ID = 'vyur3o3fpchiu9ybckgnnr51a' # Needs to be the Spotify username, not display name

user_info = requests.get(BASE_URL + 'user/' + USER_ID, headers=headers)
print(user_info)
