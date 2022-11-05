import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
playlist_id = "2LjXB8BWlV4mTktJAGhIhM"
CLIENT_ID = "ef343b8adee34ec8b498ad31f12cf0cb"
CLIENT_SECRET = "c31210f5fed44ad2ab2e9cde0994d0c9"
REDIRECTED_URI = "http://127.0.0.1:8080/"
testing = "6rAmRxPEFY6XeFQjY218fz"
scope = "playlist-modify-private user-library-modify user-library-read"
username= "calvin2nguyen"
new_music_kpop = "37i9dQZF1DXe5W6diBL5N4"
rnb_kpop = "37i9dQZF1DX089MWxS7QW5"
token =SpotifyOAuth(scope=scope,username=username,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECTED_URI)
sp = spotipy.Spotify(auth_manager=token)

"spotify:album:6nT2VfGN07ar1vdZyJY6ox"
new_tracks = []
liked_tracks = []
current_tracks  = []
blackpink ="41MozSoPIsD1dJM0CLPjZF"



## Get existing playlist and add 
def grabUri(picked_playlist):
     results = sp.user_playlist_tracks(user=username,playlist_id=picked_playlist,fields="items")
     for i in range(len(results["items"])):
        new_tracks.append(results["items"][i]["track"]["uri"])
        

     
    
def new_music_added():
    grabUri(testing)
    sp.playlist_add_items(playlist_id=playlist_id,items=new_tracks)
    

     


def update_myplaylist():
    
    try:
        saved_tracks = sp.current_user_saved_tracks()
        for i in range(len(saved_tracks["items"])):
            liked_tracks.append(saved_tracks["items"][i]["track"]["uri"])
        
        current_playlist =sp.user_playlist_tracks(user=username,playlist_id=playlist_id)
        for i in range(len(current_playlist["items"])):
            current_tracks.append(current_playlist["items"][i]["track"]["uri"])
        ## set to remove duplicates
        updated_tracks = set(current_tracks)
    
        
        duplicates = list(set(liked_tracks).intersection(set(current_tracks)))
       
        # sp.user_playlist_remove_all_occurrences_of_tracks(user=username, playlist_id=playlist_id , tracks=duplicates)
        if len(duplicates) != 0:
            sp.current_user_saved_tracks_delete(tracks=duplicates)
        
        if liked_tracks is not None:
            add_to_playlist(liked_tracks)
      
    except:
        print("no liked songs")

def add_to_playlist(x):
    sp.playlist_add_items(playlist_id=playlist_id, items=x)
   
         
        
        
    
    
    
    
grabUri(rnb_kpop)
update_myplaylist()


    
    

 
    




    

    


    
 







