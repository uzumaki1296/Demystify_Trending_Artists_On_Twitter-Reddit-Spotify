from pymongo import MongoClient
from urllib.parse import urlparse
from tabulate import tabulate
import requests
import pandas as pd


def getTwitterSpotifyData():
    CLIENT_ID = '7cf4b94fae0149c9ba21c0ab873cdf5c'
    CLIENT_SECRET = 'bb34642c7356494fa59a377a39c4efe2'

    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {'grant_type': 'client_credentials','client_id': CLIENT_ID,'client_secret': CLIENT_SECRET,})

    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']

    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

    BASE_URL = 'https://api.spotify.com/v1/'

    conn = MongoClient('mongodb://localhost:27017')

    db = conn.database
    collection1 = db.Twitter_Spot_26Nov
    collection2 = db.Twitter_Spot_26Nov1
    collection3 =  db.Twitter_Spot_27Nov
    Collection4 = db.Twitter_Spot_27Nov1

    count_Tracks = 0
    count_Playlists = 0
    count_Artists = 0

    artist_id = []
    Final_artist_list = []
    Url_array =[]

    for x in collection1.find():
        pl = x['url']
        for l in pl:
            u = (l['expanded_url'])
            Url_array.append(u)

    for x in collection2.find():
        pl = x['url']
        for l in pl:
            u = (l['expanded_url'])
            Url_array.append(u)

    for x in collection3.find():
        pl = x['url']
        for l in pl:
            u = (l['expanded_url'])
            Url_array.append(u)

    for x in Collection4.find():
        pl = x['url']
        for l in pl:
            u = (l['expanded_url'])
            Url_array.append(u)

    for u in Url_array:
        if "open.spotify.com/track" in u:
            parts = urlparse(u)
            directories = parts.path.strip('/').split('/')
            artist_id.append(directories[1])
            count_Tracks = count_Tracks + 1
            
            for i in artist_id:
                r = requests.get(BASE_URL + 'tracks/' + i, headers=headers)
                try:
                    for post in r.json()['album']['artists']:
                        Final_artist_list.append(post['name'])
                except:
                    pass
                    
        if "open.spotify.com/playlist" in u:
            parts = urlparse(u)
            directories = parts.path.strip('/').split('/')
            artist_id.append(directories[1])
            count_Playlists = count_Playlists + 1
            
            for i in artist_id:
                r = requests.get(BASE_URL + 'playlists/' + i, headers=headers)
                try:
                    list = r.json()['tracks']['items']
                    for post in list:
                        singer = (post['track']['album']['artists'])
                        for post in singer:
                            Final_artist_list.append(post['name'])
                except:
                    pass
                
        if "open.spotify.com/artist" in u:
            parts = urlparse(u)
            directories = parts.path.strip('/').split('/')
            artist_id.append(directories[1])
            count_Artists = count_Artists + 1
            
            for i in artist_id:
                r = requests.get(BASE_URL + 'artists/' + i, headers=headers)
                try:
                    Final_artist_list.append(post['name'])
                except:
                    pass

    print("Number of playlist : ", count_Playlists)
    print("Number of tracks : ", count_Tracks)
    print("Number of artists : ", count_Artists)
    
    return(count_Playlists, count_Tracks, count_Artists)