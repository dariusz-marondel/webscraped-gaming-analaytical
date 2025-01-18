import json
import pandas as pd

# Path to your JSON file
file_path = 'match_sample.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Extract the desired columns
participants = json_data['info']['participants']
table = [{"championName": participant['championName'], "win": participant['win']} for participant in participants]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(table)

# Print the DataFrame
print(df)
