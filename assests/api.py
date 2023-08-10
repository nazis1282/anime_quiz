import requests
import csv
from requests.api import head

url ="https://api.jikan.moe/v4/top/anime?filter=favorite&limit=25"

headers = {
    'Accept': 'application/json' ,
    'Content-Type':'application/json'
}

response = requests.request( "GET" , url , headers=headers , data={} )
myjson = response.json()
ourdata=[]
csvheader =['ID','TITLE','YEAR','SCORE']

for i in myjson['data']:
    listing=[i['mal_id'],i['title'],i['year'],i['score'],]
    ourdata.append(listing)


with open('anime_data.csv','w',encoding='UTF8',newline='') as f:
  writer=csv.writer(f)
  
  writer.writerow(csvheader)
  writer.writerows(ourdata)
print('done')