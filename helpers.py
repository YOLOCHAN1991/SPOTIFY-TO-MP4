import os
import requests
import urllib.parse

def lookup(url):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

        