import requests
import json
from config import API_KEY, STEAM_ID, EMAIL, FILENAME
from datetime import datetime
import openpyxl
from openpyxl.styles.borders import Border, Side
import ezgmail

current_datetime = datetime.now()
current_date = current_datetime.strftime('%Y-%m-%d')
current_time = current_datetime.strftime('%H:%M:%S')
url = f'https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={API_KEY}&steamid={STEAM_ID}&format=json '
response = requests.get(url)
# Setup the Excel sheet
wb = openpyxl.load_workbook(f'{FILENAME}')
sheet = wb.active
max = sheet.max_row
# All Columns should have an equal max_row
#
# {FILENAME} Column Cheatsheet
# A=Date B=Time C=Game D=TotalHours
# E=HoursAddedSinceLastRan F=Last2WeeksHours


if response.status_code == 200:
    
    # Parse the JSON data
    data = json.loads(response.content)

    for game in data['response']['games']:
        name = game['name']
        playtime_forever = game['playtime_forever']
        playtime_2weeks = game['playtime_2weeks']
    # Start writing to workbook
    for i in ('A', 'B', 'C', 'D', 'E', 'F'):
        sheet
    

    print('Sucess. Data Fetched from API and written to workbook.')
    ezgmail.send(f'{EMAIL}', 'Sucess!', 'Data Fetched from API and written to workbook.')
else:
    ezgmail.send(f'{EMAIL}', 'Error!', 'Error fetching data from API.')
    print("Error fetching data from API.")
    
# print(current_date)
# print(current_time)
# print(current_datetime)
# !! works !!
