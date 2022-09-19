import sys
from typing import Optional
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
def download_track_bestaudio(link, save_path):
    
    while True:
        try: 
            # object creation using YouTube
            # which was imported in the beginning 
            yt = YouTube(link, on_progress_callback=on_progress)
            best_match = yt.streams.filter(type="audio", mime_type="audio/mp4")
            file_path = best_match[-1].download(output_path=save_path, max_retries=3)
        except: 
            print('Connection Error')
            break
        else:
            return file_path
    return None

# Get video id from Search method and concatenates it with youtube watch link.
def splink_to_ytlink(spotify, spotify_link:str):
    search_query = lookup(spotify, spotify_link)

    yt_search = Search(search_query["artist"] + " - " + search_query["name"]).results
    yt_search = re.search(r"videoId=(.+)>$", str(yt_search[0])).groups()[0]
    return "https://www.youtube.com/watch?v=" + yt_search


# Function to get client_id and secret_id from Ids.txt file. For oauth
def get_ids():
    Ids = {}
    with open('ids.txt', 'r') as file:
        for line in file:
            try:
                (key, value) = line.split(":")
                Ids[key] = value.replace("\n","").strip()
            except ValueError:
                pass
    if len(Ids) > 2:
        print("Something went wrong. Ids.txt-Format:")
        print("client_id:[put client id here]")
        print("secret_id:[put secret id here]")

    for key in Ids:
        try:
            Ids[key]
        except:
            print("Something went wrong. Ids.txt-Format:")
            print("client_id:[put client id here]")
            print("secret_id:[put secret id here]")
            sys.exit()

    return Ids

# Search for playlist. Return a tracks' List
def search_playlist(spotify, playlist):
    try:
        d = spotify.playlist_tracks(playlist)
    except:
        print("Wrong Playlsit URL")
        return None

    tracks = []
    for track in d["items"]:
        tracks.append(track["track"]["external_urls"]["spotify"])
    return tracks

# Download playlist at higuest audio quality
def download_playlist(spotify, tracks: list, save_path: Optional[str] = None, res: Optional[str] = None):

    for track in tracks:
        path = download_track_bestaudio(splink_to_ytlink(spotify, track), save_path)
    print(path)
    