#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install spotipy')


# In[2]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# In[3]:


client_credentials_manager=SpotifyClientCredentials(client_id="2a0453da17da4eadae565de47a18dec6", client_secret= "d5242d01f3f94474af2a64d72a56e445")


# ## object creation
# 

# In[4]:


sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# In[5]:


playlist_link = "https://open.spotify.com/playlist/4zzUm9eZmeb4t4nUCaNoo5"


# In[6]:


playlist_link.split("/")


# In[7]:


playlist_link.split("/")[-1]


# In[8]:


playlist_URI = playlist_link.split("/")[-1]


# ## JSON Info of songs

# In[9]:


sp.playlist_tracks(playlist_URI)


# In[10]:


data = sp.playlist_tracks(playlist_URI)


# ## data transformation ( song, artist, album)

# In[11]:


data['items']


# In[12]:


len(data['items'])


# In[13]:


data['items'][0]['track']['album']['id']


# In[14]:


data['items'][0]['track']['album']['name']


# In[15]:


data['items'][0]['track']


# In[16]:


data['items'][0]['track']['album']['release_date']


# In[17]:


data['items'][0]['track']['album']['total_tracks']


# In[18]:


data['items'][0]['track']['album']['external_urls']['spotify']


# In[19]:


album_list = []
for row in data['items']:
    album_id =row['track']['album']['id']
    album_name =row['track']['album']['name']
    album_release_date =row['track']['album']['release_date']
    album_total_tracks =row['track']['album']['total_tracks']
    album_url =row['track']['album']['external_urls']['spotify']
    
    album_elements = { 'album_id': album_id, 'name':album_name, 'release_date':album_release_date, 
                      'total_tracks': album_total_tracks, 'url': album_url}
    
    album_list.append(album_elements)
    


# In[40]:


album_list


# In[20]:


data['items'][2]['track']['artists']


# In[21]:



artist_list = []
for row in data['items']:
    for key,value in row.items():
        if key == "track":
            for artist in value['artists']:
                artist_dict= {'artist_id':artist['id'], 'artist_name':artist['name'], 'external_url': artist['href']}
                artist_list.append(artist_dict)


# In[31]:


artist_list


# In[32]:


data['items'][0]['track']


# In[24]:


songs list = []
for row in data['items']:


# In[47]:


data['items'][0]['track']


# In[39]:


data['items'][0]['track']['name']


# In[72]:


song_list = []
for row in data['items']:
    song_id =  row['track']['id']
    song_name= row['track']['name']
    song_duration= row['track']['duration_ms']
    song_url= row['track']['external_urls']['spotify']
    song_popularity = row['track']['popularity']
    song_added = row['added_at']
    album_id = row['track']['album']['id']
    artist_id = row['track']['album']['artists'][0]['id']
    song_element = {'song_id': song_id,'song_name': song_name, 'duration_ms': song_duration, 'url': song_url,
                   'popularity': song_popularity, 'song_added': song_added, 'album_id': album_id, 'artist_id':artist_id}
    song_list.append(song_element)
    


# In[73]:


song_list


# In[51]:


import pandas as pd
album_df = pd.DataFrame.from_dict(album_list)


# In[52]:


album_df


# In[53]:


artist_df = pd.DataFrame.from_dict(artist_list)


# In[54]:


artist_df


# In[76]:


songs_df = pd.DataFrame.from_dict(song_list)


# In[77]:


songs_df


# In[57]:


album_df = album_df.drop_duplicates(subset =['album_id'])


# In[58]:


album_df


# In[63]:


artist_df = artist_df.drop_duplicates(subset =['artist_id'])


# In[64]:


album_df 


# In[65]:


songs_df = songs_df.drop_duplicates(subset =['song_id'])


# In[78]:


songs_df


# In[79]:


album_df.info()


# In[82]:


album_df['release_date']


# In[83]:


album_df['release_date'] = pd.to_datetime(album_df['release_date'])


# In[92]:


songs_df.info()


# In[91]:


songs_df['song_added'] = pd.to_datetime(songs_df['song_added'])


# In[93]:


artist_df.info()


# In[ ]:




