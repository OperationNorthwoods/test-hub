import requests
import json
from config import API_KEY, STEAM_ID
import shelve
from datetime import datetime

current_datetime = datetime.now()
current_date = current_datetime.strftime('%Y-%m-%d')
current_time = current_datetime.strftime('%H:%M:%S')
url = f'https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={API_KEY}&steamid={STEAM_ID}&format=json '
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON data
    data = json.loads(response.content)

    for game in data['response']['games']:
        name = game['name']
        playtime = game['playtime_forever']
        hours = round((playtime / 60), 2)
        print(name, hours)
else:
    print("Error fetching data from API")
    
# print(current_date)
# print(current_time)
# print(current_datetime)
# !! works !!
