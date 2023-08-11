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

    anchor = soup.find('div', {'class': 'information-block di-ib clearfix'})
    studio = anchor.find('span', {'class': 'information studio author'})

    name = studio.find('a').text
    data.append([name])

result_df = pd.DataFrame(data, columns=['Studio'])

animedata = pd.concat([animedata, result_df], axis=1)

animedata.to_csv('anime_data.csv', index=False)
