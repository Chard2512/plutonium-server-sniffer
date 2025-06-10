import requests
from bs4 import BeautifulSoup
import time
import winsound

url = "https://getserve.rs/t4sp"
headers = {'User-Agent': 'Mozilla/5.0'}

while True:
    print("Retrieving t4sp servers...")
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table')

        found = False

        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if columns:
                num_players = int(columns[4].text.strip()[0])
                game = columns[6].text.strip()
                if game == "Nacht Der Untoten" and (4 > num_players > 0):
                    found = True
                    print([col.text.strip() for col in columns])
                    winsound.Beep(880, 100)
    except Exception as e:
        print(f"Error: {e}")
    if found == False:
        for i in range(5, 0, -1):
            print(f"Waiting {i}s... ", end="\r")
            time.sleep(1)
    else:
         for i in range(60, 0, -1):
            print(f"Waiting {i}s... ", end="\r")
            time.sleep(1)