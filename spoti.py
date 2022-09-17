import os
import sys
import json
import requests
import cowsay
import re
import webbrowser
import spotipy
from cgi import print_exception
from helper import lookup, download_audio, parse_videoId, get_ids
from pytube import Search, YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 
from spotipy.oauth2 import SpotifyClientCredentials



save_path = 'C:/Users/POPOCHAN1990/Desktop'
link = "https://www.youtube.com/watch?v="

ids = get_ids()

try:
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=ids["client_id"], client_secret=ids["client_secret"]))
except:
    print("Spotify connection timeout. Possible causes: Internet slow, Ids wrong.")
results = lookup(spotify, "https://open.spotify.com/track/41P6Tnd8KIHqON0QIydx6a?si=4599f843bc0d4638")

download_audio(parse_videoId(results["artist"] + " - " + results["name"]))



