import os
import sys
import json
import requests
import cowsay
import webbrowser
import spotipy
from pytube import Search, YouTube
from spotipy.oauth2 import SpotifyClientCredentials
from helper import lookup
from pytube.cli import on_progress,display_progress_bar #this module contains the built in progress bar. 




save_path = 'C:/Users/POPOCHAN1990/Desktop'
dictlink = {"itag" : "0" ,"url":'https://www.youtube.com/watch?v=SmBzqkgdH9I&list=RDSmBzqkgdH9I&start_radio=1'}
link = "https://www.youtube.com/watch?v=SmBzqkgdH9I"

while True:
    try: 
        # object creation using YouTube
        # which was imported in the beginning 
        yt = YouTube(link, )
        t = yt.streams.filter(only_audio=True)
        t[0].download(save_path)
    except: 
        print("Connection Error")
        break
    else:
        break



cid = "e9137ae5cdcd40c9818981a8739f66ce"
secret = "8e16ecbe885342ef9021eb43be3c89b8"

client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
results = spotify.track('https://open.spotify.com/track/41P6Tnd8KIHqON0QIydx6a?si=4599f843bc0d4638')
results = lookup(spotify, "https://open.spotify.com/track/41P6Tnd8KIHqON0QIydx6a?si=4599f843bc0d4638")

#print(json.dumps(results, indent=2))
#webbrowser.open(results['url'])

