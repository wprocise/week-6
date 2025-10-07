## Exercise 1
"""
    Download the .env file 
    and added to the .gitignore;
    Then create python class 'Genius' and connect
    to the access token in the .env file
"""

from dotenv import load_dotenv
import os
load_dotenv('week-6.env')

class Genius:
    def __init__(self):
        self.access_token = os.getenv('ACCESS_TOKEN')
"""
    Should print the access token
"""
genius = Genius()
print(f"Access token set to: {genius.access_token}")

# Output: ACCESS_TOKEN: vw58dWIGES4DS1hb7pYPdbSyEIR_klztMKLcOgK3HtH2qFCn9EESV5p7xs96IiQc

## Exercise 2

"""
    Define genius class and retrieve access token;
    Search for artist and get the first hit's artist ID
"""
import requests
class Genius:
    def __init__(self):
        self.access_token = os.getenv('ACCESS_TOKEN')
    def get_artist(self, search_term):
        search_url = f"http://api.genius.com/search?q={search_term}&access_token={self.access_token}"
        response = requests.get(search_url)
        json_data = response.json()
      
        """
            Extract the artist ID from the first hit
        """
        artist_id = json_data['response']['hits'][0]['result']['primary_artist']['id']
        """
            Use the artist ID to get the artist information"""
        artist_url = f"http://api.genius.com/artists/{artist_id}?access_token={self.access_token}"
        artist_response = requests.get(artist_url)
        artist_data = artist_response.json()
        """
            Return the resulting JSON object
        """
        return artist_data
genius = Genius()
artist_info = genius.get_artist("Missy Elliott")
print(artist_info) # should print the JSON object with artist information

# Output: JSON object with artist information for Missy Elliott

## Exercise 3
"""
    Use the Genius class to get artist information
    and convert it to a pandas DataFrame
"""
import requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv('week-6.env')

class Genius:
    def __init__self():
        self.access_token = os.getenv('ACCESS_TOKEN')
    """
        New method to get artist information for a list of search terms
        Getting artist information using the get_artist method
        and converting the JSON response to a pandas DataFrame
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
# Output: DataFrame with artist details for the search terms with columns: search_term, artist_name, artist_id, follower_count



