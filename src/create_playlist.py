import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import pandas as pd
from config import SPOTIFY_USERNAME, PLAYLIST_NAME

# Load environment variables from .env
load_dotenv()

# Set Spotify credentials from environment variables
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# Check if they are loaded correctly
if not SPOTIPY_CLIENT_ID or not SPOTIPY_CLIENT_SECRET or not SPOTIPY_REDIRECT_URI:
    raise ValueError("Spotify API credentials not found. Check your .env file.")

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-modify-public"
))

print("Spotify authentication successful!")

def create_playlist():
    """Creates a new Spotify playlist and returns the playlist ID."""
    playlist = sp.user_playlist_create(user=SPOTIFY_USERNAME, name=PLAYLIST_NAME, public=True)
    return playlist["id"]

def add_songs_to_playlist(playlist_id, song_uris):
    """Adds songs to a Spotify playlist in batches of 100."""
    for i in range(0, len(song_uris), 100):
        batch = song_uris[i : i + 100]
        sp.playlist_add_items(playlist_id, batch)
        time.sleep(1)  # Avoid hitting API rate limits

if __name__ == "__main__":
    df = pd.read_csv("data/filtered_songs_EXPANDED.csv")  # Adjust if necessary
    song_uris = df["spotify_id"].dropna().tolist()  # Ensure column name is correct

    playlist_id = create_playlist()
    add_songs_to_playlist(playlist_id, song_uris)
    print("Songs added to playlist successfully.")
