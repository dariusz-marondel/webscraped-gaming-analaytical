import requests
import os
from dotenv import load_dotenv
import sqlite3

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
CREATE TABLE IF NOT EXISTS summoners_ids (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summ_id_encr TEXT UNIQUE NOT NULL
    puu_id_encr TEXT UNIQUE NULL);
'''

main_db = sqlite3.connect(r'/sqlite_database/project_database.db')
cursor = main_db.cursor()

# Insert data into table
for summ_id in summoner_ids:
    cursor.execute('''
    INSERT OR IGNORE INTO summoners_ids (summ_id_encr)
    VALUES (?)
    ''', (summ_id,))

# Commit the changes and close the connection
main_db.commit()
main_db.close()


print("Data insertion complete.")
