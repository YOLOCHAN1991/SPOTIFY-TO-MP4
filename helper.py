import sys
import requests
import re
from pytube import YouTube, Search
from pytube.cli import on_progress
from cgi import print_exception

# Function to search track and parse from spotify link (Requires further improvement)
def lookup(spotify, url):
    """Look up quote for symbol."""

    # Contact API
    try:
        song = spotify.track(url)
    except requests.RequestException:
        return None

    # Parse response
    try:
        return {
            "url": song["external_urls"]["spotify"],
            "artist": song["artists"][0]["name"],
            "name": song["name"],
            "uri": song["uri"],
            "id": song["id"],
            "type": song["type"],
            "href": song["href"],

        }
    except (KeyError, TypeError, ValueError):
        return None

# Function that downloads the best quality audio from yotube link.
def download_audio(link, save_path):
    while True:
        try: 
            # object creation using YouTube
            # which was imported in the beginning 
            yt = YouTube(link, on_progress_callback=on_progress)
            t = yt.streams.filter(type="audio", mime_type="audio/mp4")
            t[-1].download(output_path=save_path, max_retries=3)
        except: 
            print('Connection Error')
            break
        else:
            break
    print(type(rr),"\n", type(rt),"\n", kk)

# Get video id from Search method. Video id is the value needed to the watch key in the youtube url.
def parse_videoId():
    yt_search = Search("Julieta - Paulo Londra").results
    yt_search = re.search(r"videoId=(.+)>$", str(yt_search[0])).groups()[0]

# Function to get client_id and secret_id from Ids.txt file. For oauth
def get_ids():
    Ids = {}
    with open('ids.txt', 'r') as file:
        for line in file:
            (key, value) = line.split(":")
            Ids[key] = value.replace("\n","")
    print(Ids)