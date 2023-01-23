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


print(__file__)
savepath = os.path.dirname(os.path.realpath("config.txt"))
print(savepath)