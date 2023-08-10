import requests
from bs4 import BeautifulSoup
import pandas as pd

animedata = pd.read_csv("anime_data.csv", index_col=False)
data = []

url = 'https://myanimelist.net/anime/'
ids = animedata.ID.tolist()
for id in ids:
    r = requests.get(url + str(id))
    soup = BeautifulSoup(r.content, 'html.parser')

    anchor = soup.find('div', {'class': 'detail-characters-list clearfix'})
    characters = anchor.findAll('h3', {'class': 'h3_characters_voice_actors'})

    for i in characters:
        name = i.find('a').text
        data.append([id, name])

df = pd.DataFrame(data, columns=['ANIME_ID', 'NAME'])
df.to_csv('characters.csv', index=False)
