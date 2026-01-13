import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY=os.getenv("API_KEY")

CHANNEL="MrBeast"

def get_playlist_id():

    try:
        url=f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL}&key={API_KEY}"

        response=requests.get(url)
        response.raise_for_status()

        data=response.json()
        #print(json.dumps(data,indent=4))

        Channel_Items = data['items'][0]
        Channel_PlaylistId = Channel_Items['contentDetails']['relatedPlaylists']['uploads']
        print(Channel_PlaylistId)
        return Channel_PlaylistId
    except requests.exceptions.RequestExceptions as e:
        raise e

if __name__ == "__main__":
    get_playlist_id()