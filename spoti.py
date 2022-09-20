import os
import keyboard
import sys
import cowsay
from SpottoYou import SpottoYou, get_config





save_path = 'C:/Users/POPOCHAN1990/Desktop'
link = "https://www.youtube.com/watch?v="
sp_song_link = "https://open.spotify.com/track/5CmIIBRVQWLX2uXAkuBlS8?si=23d548dc17bd45d6"

config = get_config()

try:
    spotify = SpottoYou(config["client_id"], config["client_secret"])
except:
    print("Spotify connection timeout. Possible causes: Internet slow, config is wrong.")

print(spotify.save_path)

spotify.download_playlist(spotify.splink_to_ytlink(sp_song_link))