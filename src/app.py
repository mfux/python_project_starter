from flask import Flask
import json
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG)

from main import fetch_artist
from caching import fetch_if_not_cached

app = Flask(__name__)


# TODO: Add param to rehydrate cache
@app.route("/artists/<int:artist_id>")
def get_artist(artist_id):

    cache_path = Path(f"cache/artists/{artist_id}.json")

    artist = fetch_if_not_cached(cache_path, fetch_artist, artist_id)

    return artist
