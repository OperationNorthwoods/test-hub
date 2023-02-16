import requests
import json
from config import API_KEY, STEAM_ID, EMAIL
import shelve
from datetime import datetime
import openpyxl
import ezgmail

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
        playtime_forever = game['playtime_forever']
        playtime_2weeks = game['playtime_2weeks']

        # hours = round((playtime / 60), 2)
        # print(name, hours)
    
    print('Sucess. Data Fetched from API and written to workbook.')
    ezgmail.send(f'{EMAIL}', 'Sucess!', 'Data Fetched from API and written to workbook.')
else:
    ezgmail.send(f'{EMAIL}', 'Error!', 'Error fetching data from API.')
    print("Error fetching data from API.")
    
# print(current_date)
# print(current_time)
# print(current_datetime)
# !! works !!
