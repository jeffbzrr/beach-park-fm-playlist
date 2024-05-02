import requests
from datetime import datetime
from bs4 import BeautifulSoup
import time
import mysql.connector

import config

url = 'http://www.radioideal.net:8026/played.html'
headers = {
            'Content-Type': 'text/html',
            'User-Agent' : 'Mozilla/5.0',
        }

s = requests.session()

mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database
)
mycursor = mydb.cursor(buffered=True)


while(True):
    try:
        data = s.get(url, headers=headers)
        s.close()

        soup = BeautifulSoup(data.text, "html.parser")
        table = soup.find(text="Song Title").find_parent("table")
    
        played_list = []
        for row in table.find_all("tr")[1:]:
            row_parsed = [cell.get_text(strip=True) for cell in row.find_all("td")]
            played_list.append(row_parsed)
    
        raw = played_list[0][1].replace("\'","\\\'")

        if ' - ' in raw:
            artist = raw.split(' - ')[0]

            track = raw.split(' - ')[1]
            if track[len(track)-4:].isnumeric():
                track = track[:-5]
        else:
            artist = ''
            track = ''

        now = datetime.now()
        datetime_played = now.strftime("%Y-%m-%d ") + played_list[0][0]
    
        sql = f"INSERT INTO musics (artist, track, raw, datetime_played) VALUES ('{artist}', '{track}', '{raw}', '{datetime_played}')"

        mycursor.execute(sql)
        mydb.commit()
    except Exception as e:
        print(e)

    time.sleep(60)