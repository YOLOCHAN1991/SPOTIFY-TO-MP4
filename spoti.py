#IGNORE THIS FILE. I used this file to do some testings.

import os
import keyboard
import sys
import cowsay
from SpottoYou import SpottoYou, get_config





link = "https://www.youtube.com/watch?v=bX3S-_jUauc&list=RDMMs3Qe_yRVDuU&index=4&t=109s"
sp_song_link = "https://open.spotify.com/track/5CmIIBRVQWLX2uXAkuBlS8?si=23d548dc17bd45d6"

config = get_config()

try:
    spotify = SpottoYou(config["client_id"], config["client_secret"])
except:
    print("Spotify connection timeout. Possible causes: Internet slow, config is wrong.")

print(spotify.save_path)

spotify.download_track_bestaudio(link)