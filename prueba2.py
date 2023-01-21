from dataclasses import field
import os
import sys
import json
import requests
import cowsay
import configparser
import re
import webbrowser
import spotipy
from SpottoYou import SpottoYou, get_config
from cgi import print_exception
from helper import download_track_bestaudio, lookup,search_playlist, download_playlist, splink_to_ytlink, get_ids
from pytube import Search, YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 
from spotipy.oauth2 import SpotifyClientCredentials



save_path = 'C:/Users/POPOCHAN1990/Desktop'
link = "https://www.youtube.com/watch?v="
sp_song_link = "https://open.spotify.com/track/5CmIIBRVQWLX2uXAkuBlS8?si=23d548dc17bd45d6"

config = get_config()

client_id='e9137ae5cdcd40c9818981a8739f66ce'
client_secret='8e16ecbe885342ef9021eb43be3c89b8'




spotify = SpottoYou(config["client_id"], config["client_secret"], config["save_path"])

spotify.download_playlist("https://open.spotify.com/playlist/37i9dQZF1E8KJg3WkXQbZu?si=3c8b199871104724")