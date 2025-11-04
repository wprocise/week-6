import os
import requests
import pandas as pd
from typing import Optional, List, Dict
from dotenv import load_dotenv

# Load .env if available
load_dotenv("week-6.env")


class Genius:
    """
    Minimal Genius API wrapper for exercises and testing.
    """

    def __init__(self, access_token: Optional[str] = None):
        # Prefer explicit token, fallback to environment
        if access_token is None:
            access_token = os.getenv("ACCESS_TOKEN")
        self.access_token = access_token

    def _get(self, url: str, params: Dict = None) -> Dict:
        """Internal helper to make GET requests with Authorization header."""
        headers = {}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"

        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()  # Let tests catch HTTP errors
        return response.json()

    def get_artist(self, search_term: str) -> Dict:
        """
        Search Genius for an artist by name.
        Returns parsed JSON from the /artists/{id} endpoint or {} if not found.
        """
        if not isinstance(search_term, str) or not search_term.strip():
            raise ValueError("search_term must be a non-empty string")

        search_url = "https://api.genius.com/search"
        search_json = self._get(search_url, params={"q": search_term})

        hits = search_json.get("response", {}).get("hits", [])
        if not hits:
            return {}

        artist_id = hits[0].get("result", {}).get("primary_artist", {}).get("id")
        if not artist_id:
            return {}

        artist_url = f"https://api.genius.com/artists/{artist_id}"
        return self._get(artist_url)

    def get_artists(self, search_terms: List[str]) -> pd.DataFrame:
        """
        Accepts a list of search terms and returns a DataFrame with:
        ['search_term', 'artist_name', 'artist_id', 'follower_count']
        """
        if not isinstance(search_terms, (list, tuple)):
            raise ValueError("search_terms must be a list or tuple")

        records = []
        for term in search_terms:
            artist_data = {
                "search_term": term,
                "artist_name": None,
                "artist_id": None,
                "follower_count": None
            }

            try:
                json_data = self.get_artist(term)
            except requests.HTTPError:
                records.append(artist_data)
                continue

            artist_obj = json_data.get("response", {}).get("artist")
            if artist_obj:
                artist_data["artist_name"] = artist_obj.get("name")
                artist_data["artist_id"] = artist_obj.get("id")
                artist_data["follower_count"] = artist_obj.get("followers_count")

            records.append(artist_data)

        return pd.DataFrame(records)


# Only runs if file executed directly, not when imported by tests
if __name__ == "__main__":
    g = Genius()
    print("Token loaded:", bool(g.access_token))
    # Manual check (commented to avoid accidental live calls)
    # print(g.get_artist("Missy Elliott"))
    # print(g.get_artists(["Drake", "Taylor Swift"]))













