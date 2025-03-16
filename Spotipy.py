import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os 

client_id = "d9745bec4fe042b3a496a7fe7bc0f206"
client_secret = "3fc82434ab934ac083304dd7f436b196"

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


def getTrackIDs(user, playlist_id):
    track_ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        track_ids.append(track['id'])
    return track_ids

def getTrackFeatures(id):
    track_info = sp.track(id)

    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']

    track_data = [name, album, artist]
    return track_data


emotion_dict = {0:"Angry",1:"Disgusted",2:"Fearful",3:"Happy",4:"Neutral",5:"Sad",6:"Surprised"}
music_dist={0:"6b9wAfboIaotJyUElxw0Yt",1:"1hTS8rXKwOpWu3n85cF0HB",2:"2BcV8OdmOXTje8JBh0M0bl",3:"34e9pfPINRKBbV6EH9OlIi",4:"3IOtLAzuWuCy9Qt6wpzgWt",5:"34Cw11mYramy2de7xvElZJ",6:"2hX72029InsnAVQIPsxzOE"}

# Run if u dont want to generate the csv files again and comment the codes of csv generation that are written below this code 
# def generate_csv(emotion_index):
#     """ Generate CSV only if it does not exist """
#     filename = f'songs/{emotion_dict[emotion_index].lower()}.csv'
#     if os.path.exists(filename):
#         print(f"CSV file already exists: {filename}")
#         return  # Skip generation if file already exists

#     track_ids = getTrackIDs('spotify', music_dist[emotion_index])
#     track_list = []
#     for i in range(len(track_ids)):
#         time.sleep(.3)
#         track_data = getTrackFeatures(track_ids[i])
#         track_list.append(track_data)

#     df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist'])
#     df.to_csv(filename, index=False)
#     print(f"CSV Generated: {filename}")

# # Generate CSVs only if not present
# for i in range(7):  # Loop for 7 emotion categories
#     generate_csv(i)

track_ids = getTrackIDs('spotify',music_dist[0])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) 
print("CSV Generated")

track_ids = getTrackIDs('spotify',music_dist[1])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) 
    df.to_csv('songs/disgusted.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify',music_dist[2])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) 
    df.to_csv('songs/fearful.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify',music_dist[3])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) 
    df.to_csv('songs/happy.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify',music_dist[4])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns = ['Name','Album','Artist'])
    df.to_csv('songs/neutral.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify',music_dist[5])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns = ['Name','Album','Artist'])
    df.to_csv('songs/sad.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify',music_dist[6])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) 
    df.to_csv('songs/surprised.csv')
print("CSV Generated")