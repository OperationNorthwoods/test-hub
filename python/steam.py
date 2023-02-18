import requests
import json
from config import API_KEY, STEAM_ID, EMAIL, FILENAME
from datetime import datetime
import openpyxl
from openpyxl.styles.borders import Border, Side
import ezgmail

# setting up seperate date and time variables
current_datetime = datetime.now()
current_date = current_datetime.strftime('%Y-%m-%d')
current_time = current_datetime.strftime('%H:%M:%S')
# api call url
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

if response.status_code == 200: # 200 = it worked
    
    # Parse the JSON data
    data = json.loads(response.content)

    gameCounter = 0 # counts number of games in json response
    gameDict = {}

    for game in data['response']['games']:
        gameCounter+=1
        name = game['name']
        playtime_forever = game['playtime_forever']
        playtime_2weeks = game['playtime_2weeks']
        gameDict[name] = (playtime_forever, playtime_2weeks)
        
    # Start writing to workbook
    max_Iter = max + 1  # make sure we don't go too far down rows
    col_A, col_B, col_C, col_D, col_E, col_F = range(1, 7)
    temp = list(gameDict.keys()) # makes 
    tempCount = 0

    # main writing loop. loops throught all columns, one row at a time.
    while max_Iter <= max+gameCounter:
        sheet.cell(row=max_Iter, column=col_A, value=current_date)
        sheet.cell(row=max_Iter, column=col_B, value=current_time)
        sheet.cell(row=max_Iter, column=col_C, value=temp[tempCount])
        sheet.cell(row=max_Iter, column=col_D, value=gameDict[temp[tempCount]][0])
        sheet.cell(row=max_Iter, column=col_F, value=gameDict[tempCount][1])

        if max_Iter <= max+gameCounter:
            print('put bottom border stuff here')

        tempCount+=1
        max_Iter+=1
            

    

    print('Sucess. Data Fetched from API and written to workbook.')
    ezgmail.send(f'{EMAIL}', 'Sucess!', 'Data Fetched from API and written to workbook.')
else:
    ezgmail.send(f'{EMAIL}', 'Error!', 'Error fetching data from API.')
    print("Error fetching data from API.")
    
# print(current_date)
# print(current_time)
# print(current_datetime)
# !! works !!
