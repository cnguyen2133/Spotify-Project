import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
playlist_id = "2LjXB8BWlV4mTktJAGhIhM"
CLIENT_ID = "ac0e5b1c8c5740eb94eb2ac65433be34"
CLIENT_SECRET = "83a24f0ffa044d48ab811c99deb714dd"
REDIRECTED_URI = "http://127.0.0.1:8080/"
testing = "6rAmRxPEFY6XeFQjY218fz"
scope = "playlist-modify-private"
username= "calvin2nguyen"
new_music_kpop = "37i9dQZF1DXe5W6diBL5N4"
rnb_kpop = "37i9dQZF1DX089MWxS7QW5"
token =SpotifyOAuth(scope=scope,username=username,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECTED_URI)
sp = spotipy.Spotify(auth_manager=token)

"spotify:album:6nT2VfGN07ar1vdZyJY6ox"
new_tracks = []
liked_tracks = []
blackpink ="41MozSoPIsD1dJM0CLPjZF"



## Get existing playlist and add 
def grabUri(picked_playlist):
     results = sp.user_playlist_tracks(user=username,playlist_id=picked_playlist,fields="items")
     for i in range(len(results["items"])):
        new_tracks.append(results["items"][i]["track"]["uri"])
        

     
    
def new_music_added():
    grabUri(testing)
    sp.playlist_add_items(playlist_id=playlist_id,items=new_tracks)
    

def liked_music():
    asdf =sp.user_playlist_tracks(user=username,playlist_id=playlist_id)
    for i in range(len(asdf["items"])):
        print(asdf["items"][i]["track"]["uri"])

    saved_tracks = sp.current_user_saved_tracks()
    
    for i in range(len(saved_tracks["items"])):
        print(saved_tracks["items"][i]["track"]["uri"])
        liked_tracks.append(saved_tracks["items"][i]["track"]["uri"])
        
    fff = list(map(lambda x,y: (x == y) ,asdf,saved_tracks))
    print(fff)
    
    # sp.playlist_add_items(playlist_id=playlist_id, items=liked_tracks)
    
    # offset = 0
    # while(offset < len(tracks)):
    #     print([k for k ,v in liked_playlist.items() if v == True])
    #     offset +=30
       
    
   
         
        
        
    
    
    
    
grabUri(rnb_kpop)
liked_music()


    
    

 
    




    

    


    
 







