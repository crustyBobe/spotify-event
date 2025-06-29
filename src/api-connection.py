import requests
import os
import json

# from auth import headers

# Set auth credentials
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

# Set users's ID. TODO: Get ID from user input and verify
USER_ID = 'vyur3o3fpchiu9ybckgnnr51a' # Needs to be the Spotify username, not display name

access_token = '' # See return value from auth.py
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Returns the user's top artists or tracks, based on passed 'type'. Requires user-top-read
def get_top(type):
    if type.lower() not in ['artists', 'tracks']: # Currently API only works for artists and tracks
        raise ValueError("Wrong type passed. Must be either 'tracks', or 'artists'")
    response_json = requests.get(BASE_URL + 'me/top/' + type.lower(), headers=headers).json()
    return ([track['name'] for track in response_json['items']])

# Returns user's followed artists. Requires user-follow-read
def get_following():
    response_json = requests.get(BASE_URL + 'me/following?type=artist', headers=headers).json()
    return response_json # Update response to only return followed artists names
