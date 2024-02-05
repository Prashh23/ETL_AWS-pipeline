#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime



# In[ ]:


def lambda_handler(event, context):
    # TODO implement
    client_credentials_manager=SpotifyClientCredentials(client_id="2a0453da17da4eadae565de47a18dec6", client_secret= "d5242d01f3f94474af2a64d72a56e445")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlist_link = "https://open.spotify.com/playlist/4zzUm9eZmeb4t4nUCaNoo5"
    playlist_URI = playlist_link.split("/")[-1]
    
    spotify_data=sp.playlist_tracks(playlist_URI)
    print(spotify_data)
    
    
    client = boto3.client("s3")
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    client.put_object(
        Bucket= "spotify-etl-prash",
        Key = "raw_data/to_processed/" + filename,
        Body = json.dumps(spotify_data)
        )

