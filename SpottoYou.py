from logging import raiseExceptions
import os
import sys
import keyboard
import requests
import re
import spotipy
from typing import Any, Optional
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube, Search
from pytube.cli import on_progress
from cgi import print_exception





class SpottoYou():

    def __init__(self, cid, cs, save_path:Optional[str] = None) -> None:
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=cs))
        self._save_path = save_path

    @property
    def save_path(self):
        if os.path.isdir(str(self._save_path)):
            return self._save_path
        self._save_path = os.path.dirname(os.path.realpath(__file__))
        return self._save_path


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
    
    def download_track_bestaudio(self, yt_link):

        while True:
            try:
                # object creation using YouTube
                # which was imported in the beginning 
                yt = YouTube(yt_link, on_progress_callback=on_progress)
                best_match = yt.streams.filter(type="audio", mime_type="audio/mp4")
                file_path = best_match[-1].download(output_path=self.save_path, max_retries=3)
            except:
                print_exception()
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



    # Search for playlist. Return the tracks' List
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

    # Download playlist at higuest audio quality.
    def download_playlist(self, playlist: list):
        tracks = self.search_playlist(playlist)
        for track in tracks:
            try:
                path = self.download_track_bestaudio(self.splink_to_ytlink(track), self.save_path)
            except:
                pass
        print("Playlist installed at", path)

# Get config data from config.txt in dict format.
def get_config():
        configs = {}
        with open('config.txt', 'r') as file:
            for line in file:
                try:
                    (key, value) = line.split("=")
                    configs[key] = value.replace("\n","").strip()
                except ValueError:
                    pass
        if len(configs) < 2:
            print("Something went wrong. config.txt-Format:")
            input("Press any key to close")
            sys.exit()
            


        for key in configs:
            try:
                configs[key]
            except:
                print("Something went wrong. config.txt-Format:")
                input("Press any key to close")
                sys.exit()

        return configs