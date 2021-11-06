import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
os.environ['SPOTIPY_CLIENT_ID'] = 'c97c4d2a24b5431a9decec1112f2139d'
os.environ['SPOTIPY_CLIENT_SECRET'] = '4d1690c7b5764bc48ca7dab4d46b2fbf'

artist_uri = 'spotify:artist:3HqSLMAZ3g3d5poNaI7GOU'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(artist_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])