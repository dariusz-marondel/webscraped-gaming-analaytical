import os
import sqlite3
import time
import pandas as pd
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('api_key.env')
# Get API key from env file
api_key = os.getenv('API_KEY')

main_db = sqlite3.connect(r'/Users/amberlights/Repositories/simple-lol-stats/sqlite_database/project_database.db')
cursor = main_db.cursor()

puuid_list = pd.read_sql('''
SELECT puu_id
FROM summoners;
''', main_db)

# Make sure its a list
puuid_list = puuid_list['puu_id'].tolist()

start_time = 1736204400 # Last patch epoch time in seconds
end_time = int(time.time())
count = 100
headers = {
    "X-Riot-Token": api_key
}

call_count = 0
game_id_list = []

for puuid in puuid_list:

    url = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?startTime={start_time}&endTime={end_time}&type=ranked&start=0&count={count}'
    # Make the API call
    response = requests.get(url, headers=headers)

    # Handle the response
    if response.status_code == 200:
        data = response.json()
        game_id_list.extend(data)
        print(f'Called API successfully for a player {puuid} and retrieved their games')
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')
    call_count += 1
    if call_count % 20 == 0:
        time.sleep(1)
    if call_count % 100 == 0 and call_count != len(game_id_list):
        time.sleep(120)

for game_id in game_id_list:
    cursor.execute('INSERT OR IGNORE INTO games (game_id) VALUES (?)', (game_id,))

main_db.commit()
main_db.close()
