import requests
import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd
import time

# Load environment variables from .env file
load_dotenv('api_key.env')
# Get API key from env file
api_key = os.getenv('API_KEY')

main_db = sqlite3.connect(r'/Users/amberlights/Repositories/simple-lol-stats/sqlite_database/project_database.db')
cursor = main_db.cursor()

game_id_list = pd.read_sql('''
SELECT game_id
FROM games_p24
ORDER BY RANDOM()
LIMIT 10000;
''', main_db)

# Making sure we pass list of IDs in form of a list
game_id_list = game_id_list['game_id'].tolist()

headers = {
    "X-Riot-Token": api_key
}

def call_match_api(game_id):
    url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{game_id}'
    response = requests.get(url, headers=headers)
    # Handle the response
    if response.status_code == 200:
        data = response.json()
        print(f'Succesful API call for game {game_id}')
        # This API call actually returns much more data,
        # however for purpose of current state of this project there is no need to retain them
        participants = data['info']['participants']
        table = [{"champion": participant['championName'], "have_won": participant['win']} for participant in
                 participants]
        return table
    else:
        print(f'Failed to rertieve data for game {game_id}. Status code: {response.status_code}')
        return None

call_count = 0

# We store it in sqlite table created with DataGrip
'''
CREATE TABLE IF NOT EXISTS winrate_data (
    player INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id TEXT NOT NULL,
    champion TEXT NOT NULL,
    have_won INTEGER NULL CHECK (have_won = 0 OR have_won = 1)
);
'''

for i, game_id in enumerate(game_id_list):
    match = call_match_api(game_id)
    if match:
        match_df = pd.DataFrame(match)
        match_df['game_id'] = f'{game_id}'
    call_count += 1

    if call_count % 20 == 0:
        time.sleep(1)
    if call_count % 100 == 0:
        time.sleep(120)
    match_df.to_sql('winrate_data_p24', main_db, if_exists='append', index=False)
    print(f'Data insertion for game {game_id} complete.')

# Commit the changes and close the connection
main_db.commit()
main_db.close()


