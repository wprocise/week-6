from dotenv import load_dotenv
import os
import requests
import pandas as pd

# Load environment variables
load_dotenv('week-6.env')

class Genius:
    def __init__(self):
        self.access_token = os.getenv('ACCESS_TOKEN')
    """
        New method to get artist information for a list of search terms
        Getting artist information for various search terms
    """
    def get_artist(self, search_term):
        search_url = f"http://api.genius.com/search?q={search_term}&access_token={self.access_token}"
        response = requests.get(search_url)
        json_data = response.json()
        artist_id = json_data['response']['hits'][0]['result']['primary_artist']['id']
        artist_url = f"http://api.genius.com/artists/{artist_id}?access_token={self.access_token}"
        artist_response = requests.get(artist_url)
        artist_data = artist_response.json()
        return artist_data
    """
        Defining columns and creating DataFrame
        Returns DataFrame with artist details
    """
    def get_artists(self, search_terms):
        records = []
        for term in search_terms:
            artist_info = self.get_artist(term)
            artist_data = artist_info['response']['artist']
            record = {
                'search_term': term,
                'artist_name': artist_data.get('name'),
                'artist_id': artist_data.get('id'),
                'follower_count': artist_data.get('followers_count')
            }
            records.append(record)
        df = pd.DataFrame(records)
        return df
genius = Genius()
search_terms = ["Shaboozey", "Usher", "Taylor Swift", "Drake"]
df = genius.get_artists(search_terms)
print(df)
















