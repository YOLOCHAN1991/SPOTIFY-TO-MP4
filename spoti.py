import os
import sys
import json
import requests
import cowsay
import re
import webbrowser
import spotipy
from cgi import print_exception
from helper import lookup, download_audio
from pytube import Search, YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 
from spotipy.oauth2 import SpotifyClientCredentials



save_path = 'C:/Users/POPOCHAN1990/Desktop'
link = "https://www.youtube.com/watch?v="


yt_search = Search("Julieta - Paulo Londra").results
yt_search = re.search(r"videoId=(.+)>$", str(yt_search[0])).groups()[0]
link += yt_search
print(link)



cid = "e9137ae5cdcd40c9818981a8739f66ce"
secret = "8e16ecbe885342ef9021eb43be3c89b8"
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'


client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret)

spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + "Trueno", type='artist')
print(results)
results = spotify.track('https://open.spotify.com/track/41P6Tnd8KIHqON0QIydx6a?si=4599f843bc0d4638')
print(spotify)
#results = lookup(spotify, "https://open.spotify.com/track/41P6Tnd8KIHqON0QIydx6a?si=4599f843bc0d4638")

#print(json.dumps(results, indent=2))
#webbrowser.open(results['url'])

