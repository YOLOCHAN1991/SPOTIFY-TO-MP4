import requests
import sys

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

