import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
playlist_id = "2LjXB8BWlV4mTktJAGhIhM"
CLIENT_ID = "ac0e5b1c8c5740eb94eb2ac65433be34"
CLIENT_SECRET = "83a24f0ffa044d48ab811c99deb714dd"
REDIRECTED_URI = "http://127.0.0.1:8080/"

scope = "playlist-modify-private"
username= "calvin2nguyen"
new_music_kpop = "37i9dQZF1DXe5W6diBL5N4"
rnb_kpop = "37i9dQZF1DX089MWxS7QW5"
token =SpotifyOAuth(scope=scope,username=username,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECTED_URI)
sp = spotipy.Spotify(auth_manager=token)

"spotify:album:6nT2VfGN07ar1vdZyJY6ox"
tracks = []
blackpink ="41MozSoPIsD1dJM0CLPjZF"


def addTracks():

    searched_songs = sp.search(q="album:k-pop",type="artist",limit=2,market="US")
    

    formated_list =(json.dumps(searched_songs,sort_keys=4,indent=4))
    # print(formated_list)
    track_uri = searched_songs["tracks"]["items"]
    for i in range(len(track_uri)):
        tracks.append(track_uri[i]["uri"])
        
    sp.playlist_add_items(playlist_id=playlist_id,items=tracks)

def grabUri(picked_playlist):
     results = sp.user_playlist_tracks(user=username,playlist_id=picked_playlist,fields="items")
     for i in range(len(results["items"])):
        tracks.append(results["items"][i]["track"]["uri"])
        

     
        
         
     
def addtoPlaylist():
    grabUri(rnb_kpop)
    grabUri(new_music_kpop)
 
 
    
addtoPlaylist()
print(tracks)


    

    


    
 







