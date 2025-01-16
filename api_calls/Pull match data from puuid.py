import requests
import json
import pandas as pd

# Get API key from env file
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('301 API key.env')

# Access the API key
api_key = os.getenv('API_KEY')

puuid = 'xpY097aVJPACaeW_Z-TqYCkl4orU3slWfDHqerbbGo4RA18Gu7_0BWyV83ETUW-4SbN1ZC8HcsyPZw'
start_time = 1736204400
end_time = 1736960400
count = 100

url = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?startTime={start_time}&endTime={end_time}&type=ranked&start=0&count={count}'
headers = {
    "X-Riot-Token": api_key
}

# Make the API call
response = requests.get(url, headers=headers)

# Specify the filename for .json output
filename = "305 MatchIDs.json"

# Handle the response
if response.status_code == 200:
    data = response.json()
    print('Called API sucesfully')
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')

