import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
import time
import requests
main_db = sqlite3.connect(r'/sqlite_database/project_database.db')
cursor = main_db.cursor()

summoner_ids = pd.read_sql('''
SELECT summ_id_encr
FROM summoners_ids
LIMIT 300;
''', main_db)

summoner_ids = summoner_ids['summ_id_encr'].tolist()

# Load environment variables from .env file
load_dotenv('api_key.env')
# Access the API key
api_key = os.getenv('API_KEY')

headers = {
    "X-Riot-Token": api_key
}

puuid_list = []

def call_puuid_api(i, summoner_id):
    url = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}'
    response = requests.get(url, headers=headers)
    # Handle the response
    if response.status_code == 200:
        data = response.json()
        print(f'Succesful API call nr {i}')
        return data['puuid']
    else:
        print(f'Failed to rertieve data. Status code: {response.status_code}')
        return None

call_count = 0

for i, summ_id in enumerate(summoner_ids):
    puuid = call_puuid_api(i, summ_id)
    if puuid:
        puuid_list.append(puuid)
    call_count += 1

    if call_count % 20 == 0:
        time.sleep(1)
    if call_count % 100 == 0:
        time.sleep(120)
'''
# create a table using DataGrip
     
CREATE TABLE IF NOT EXISTS puu_ids(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    puu_id TEXT UNIQUE NOT NULL); '''

# Insert data into table
for puu_id in puuid_list:
    cursor.execute('''
    INSERT OR IGNORE INTO puu_ids (puu_id)
    VALUES (?)
    ''', (puu_id,))

# Commit the changes and close the connection
main_db.commit()
main_db.close()

print("Data insertion complete.")