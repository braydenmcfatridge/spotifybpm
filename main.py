import os
from pprint import pprint

import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_id = '0wibgD7mU2o1PR0i0XmvS0'
playlist_items = sp.playlist_items(playlist_id, fields='items(track(name,artists(name)))', market='US')
tracks = playlist_items['items']
# pprint(tracks)

url = 'https://api.getsongbpm.com/{}'

for track in tracks:
    artist_names = []
    artists = track['track']['artists']
    for artist in artists:
        artist_names.append(artist['name'])
    track_name = track['track']['name']
    params = {
        'api_key': os.getenv('BPM_API_KEY'),
        'type': 'song',
        'lookup': track_name,
    }
    search_resp = requests.get(url.format('search/'), params=params)
    print(search_resp.text)
    input()
