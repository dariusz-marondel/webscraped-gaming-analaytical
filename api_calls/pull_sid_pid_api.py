import os
from dotenv import load_dotenv
import requests
import sqlite3
import pandas as pd
import time


# Load environment variables from .env file
load_dotenv('api_key.env')
# Get API key from env file
api_key = os.getenv('API_KEY')

summoner_ids = []
leagues = ['DIAMOND', 'EMERALD', 'PLATINUM']
divisions = ['I', 'II', 'III', 'IV']

headers = {
    "X-Riot-Token": api_key
}

for league in leagues:
    for division in divisions:
        url = f'https://eun1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{league}/{division}?page=1'
        # Make the API call
        response = requests.get(url, headers=headers)
        # Handle the response
        if response.status_code == 200:
            data = response.json()
            print(f'Succesful API call for {league} {division}')
            for summoner in data:
                summoner_ids.append(summoner['summonerId'])
        else:
            print(f'Failed to rertieve data. Status code: {response.status_code}')

# Based on official lol stats we should have see 50k-100k players not 2460,
# obviously caused by not calling all pages for each league
# however 2,5k will be sufficient for this project

# We store it in sqlite table created with DataGrip
'''
CREATE TABLE IF NOT EXISTS summoners (
summ_id TEXT PRIMARY KEY, -- encrypted summoner id, unique for every player in specific region
puu_id TEXT UNIQUE NOT NULL, --encrypted id of every player, unique globally 
game_name TEXT, -- name used by player in game
tag_line TEXT) -- tagline used by player in game;
'''

call_count = 12
puuid_list = []

def call_puuid_api(i, summoner_id):
    url = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}'
    response = requests.get(url, headers=headers)
    # Handle the response
    if response.status_code == 200:
        data = response.json()
        print(f'Successful puuid API call nr {i}')
        return data
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')
        return None

data_list = []

for i, summ_id in enumerate(summoner_ids):
    data = call_puuid_api(i, summ_id)
    if data:
        data_list.append({
            'puu_id': data.get('puuid'),
            'summ_id': data.get('id')
        })
    call_count += 1

    if call_count % 20 == 0:
        time.sleep(1)
    if call_count % 100 == 0 and call_count != len(summoner_ids):
        time.sleep(120)

summoners_df = pd.DataFrame(data_list)


main_db = sqlite3.connect(r'/Users/amberlights/Repositories/simple-lol-stats/sqlite_database/project_database.db')
cursor = main_db.cursor()

summoners_df.to_sql('summoners', main_db, if_exists='append', index=False)

# Commit the changes and close the connection
main_db.commit()
main_db.close()


print("Players data insertion complete.")
