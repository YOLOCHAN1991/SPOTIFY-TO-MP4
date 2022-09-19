from dataclasses import field
import os
import sys
import json
import requests
import cowsay
import re
import webbrowser
import spotipy
import classtest
from cgi import print_exception
from helper import lookup, download_track_bestaudio, splink_to_ytlink, get_ids
from pytube import Search, YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 
from spotipy.oauth2 import SpotifyClientCredentials



save_path = 'C:/Users/POPOCHAN1990/Desktop'
link = "https://www.youtube.com/watch?v="
sp_song_link = "https://open.spotify.com/track/5CmIIBRVQWLX2uXAkuBlS8?si=23d548dc17bd45d6"

ids = get_ids()

try:
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=ids["client_id"], client_secret=ids["client_secret"]))
except:
    print("Spotify connection timeout. Possible causes: Internet slow, Ids wrong.")

d = spotify.playlist_tracks("https://open.spotify.com/playlist/37i9dQZF1DXaPCIWxzZwR1?si=3e60b5b6545c4739", limit=1)

print(type(d))

print(json.dumps(d["items"][0]["track"]["external_urls"]["spotify"], indent = 2))
