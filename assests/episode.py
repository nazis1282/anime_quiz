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

    anchor = soup.find(
        'div', {'class': 'di-ib form-user-episode ml8 disabled'})
    episodes_number = anchor.find('span', {'id': 'curEps'})

    if episodes_number:

        episodes = episodes_number.text

        if episodes == '?':

            episodes = 'airing'

    data.append([episodes])


result_df = pd.DataFrame(data, columns=['episodes'])

animedata = pd.concat([animedata, result_df], axis=1)

animedata.to_csv('anime_data.csv', index=False)
