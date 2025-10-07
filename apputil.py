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

