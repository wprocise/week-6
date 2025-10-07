## Exercise 1
"""
    Download the .env file 
    and added to the .gitignore
"""

from dotenv import load_dotenv
import os
load_dotenv('week-6.env')
access_token = os.getenv('GENIUS_ACCESS_TOKEN')
print(access_token)

class Genius:
    def __init__(self, access_token):
        self.access_token = access_token
        