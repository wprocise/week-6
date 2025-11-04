# Exercise 1
"""
    Download the .env file 
    and added to the .gitignore;
    Then create python class 'Genius' and connect
    to the access token in the .env file
"""

from dotenv import load_dotenv
import os
import requests
import pandas as pd

# Load environment variables
load_dotenv("week-6.env")

class Genius:
    def __init__(self):
        self.access_token = os.getenv("ACCESS_TOKEN")
        if not self.access_token:
            raise ValueError("ACCESS_TOKEN not found. Make sure it is set in week-6.env")

    def get_artist(self, search_term):
        """Returns full artist JSON object for a given search term."""
        search_url = f"https://api.genius.com/search?q={search_term}&access_token={self.access_token}"
        response = requests.get(search_url)
        json_data = response.json()

        artist_id = json_data['response']['hits'][0]['result']['primary_artist']['id']
        artist_url = f"https://api.genius.com/artists/{artist_id}?access_token={self.access_token}"
        artist_response = requests.get(artist_url)
        return artist_response.json()

    def get_artists(self, search_terms):
        """Returns a Pandas DataFrame with selected artist info."""
        records = []
        for term in search_terms:
            data = self.get_artist(term)['response']['artist']
            records.append({
                "search_term": term,
                "artist_name": data.get("name"),
                "artist_id": data.get("id"),
                "follower_count": data.get("followers_count")
            })
        return pd.DataFrame(records)


# Run only when file is executed directly (not imported)
if __name__ == "__main__":
    genius = Genius()
    search_terms = ["Shaboozey", "Usher", "Taylor Swift", "Drake"]
    df = genius.get_artists(search_terms)
    print(df)











