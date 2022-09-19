import sys
import requests
import re
import spotipy
from typing import Optional
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube, Search
from pytube.cli import on_progress
from cgi import print_exception




class SpottoYou():

    def __init__(self, cid, cs) -> None:
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=cs))

    def lookup(self, url):
        """Look up quote for symbol."""

        # Contact API
        try:
            song = self.spotify.track(url)
        except:
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
    def splink_to_ytlink(self, spotify_link:str):
        search_query = self.lookup(spotify_link)

        yt_search = Search(search_query["artist"] + " - " + search_query["name"]).results
        yt_search = re.search(r"videoId=(.+)>$", str(yt_search[0])).groups()[0]
        return "https://www.youtube.com/watch?v=" + yt_search


    # Function to get client_id and secret_id from Ids.txt file. For oauth
    def get_config():
        Ids = {}
        with open('config.txt', 'r') as file:
            for line in file:
                try:
                    (key, value) = line.split(":")
                    Ids[key] = value.replace("\n","").strip()
                except ValueError:
                    pass
        if len(Ids) < 2:
            print("Something went wrong. config.txt-Format:")


        for key in Ids:
            try:
                Ids[key]
            except:
                print("Something went wrong. config.txt-Format:")
                sys.exit()

        return Ids

    # Search for playlist. Return a tracks' List
    def search_playlist(self, playlist):
        try:
            d = self.spotify.playlist_tracks(playlist)
        except:
            print("Wrong Playlsit URL")
            return None

        tracks = []
        for track in d["items"]:
            tracks.append(track["track"]["external_urls"]["spotify"])
        return tracks

    # Download playlist at higuest audio quality
    def download_playlist(self, tracks: list, save_path: Optional[str] = None, res: Optional[str] = None):

        if res:
            self.res = res

        for track in tracks:
            path = self.download_track_bestaudio(self.splink_to_ytlink(track), save_path)
        print(path)
    

client_id='e9137ae5cdcd40c9818981a8739f66ce'
client_secret='8e16ecbe885342ef9021eb43be3c89b8'

spotify = SpottoYou(client_id, client_secret)

s = spotify.lookup("https://open.spotify.com/track/5CmIIBRVQWLX2uXAkuBlS8?si=b25676a5c4e947a2")

print(s)