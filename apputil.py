import os
import requests
import pandas as pd
from dotenv import load_dotenv


class Genius:
    """Simple wrapper around the Genius API."""

    def __init__(self, access_token=None):
        load_dotenv("week-6.env")  # safe call, no error if missing

        # prefer explicit token, fallback to environment variable
        self.access_token = access_token or os.getenv("ACCESS_TOKEN")

        if not self.access_token:
            raise ValueError("A Genius API access token is required.")

        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.access_token}"})

    def _request(self, endpoint, params=None):
        """Internal helper to call Genius API."""
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url, params=params or {})
        response.raise_for_status()
        return response.json()

    def get_artist(self, artist_id: int) -> dict:
        """Return a dictionary containing artist info: name + id."""
        data = self._request(f"/artists/{artist_id}")
        artist = data["response"]["artist"]
        return {"id": artist["id"], "name": artist["name"]}

    def get_artists(self, artist_ids: list[int]) -> pd.DataFrame:
        """Return a pandas DataFrame with columns: id, name."""
        artists = [self.get_artist(aid) for aid in artist_ids]
        return pd.DataFrame(artists)













