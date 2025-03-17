import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Authenticate with Spotify API
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Test API Call: Get Track Info for a Known Song (Use a valid Spotify track ID)
track = sp.track("3n3Ppam7vgaVa1iaRUc9Lp")  # Valid track ID for "Mr. Brightside"
print(track["name"], "by", track["artists"][0]["name"])
