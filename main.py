import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
playlist_id = "2LjXB8BWlV4mTktJAGhIhM"
CLIENT_ID = "ef343b8adee34ec8b498ad31f12cf0cb"
CLIENT_SECRET = "c31210f5fed44ad2ab2e9cde0994d0c9"
REDIRECTED_URI = "http://127.0.0.1:8080/"

new_music_playlist = "44pxs36DWyYol10pUJSMOJ"
scope = "playlist-modify-private user-library-modify user-library-read"
username= "calvin2nguyen"
new_music_kpop = "37i9dQZF1DXe5W6diBL5N4"
rnb_kpop = "37i9dQZF1DX089MWxS7QW5"
token =SpotifyOAuth(scope=scope,username=username,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECTED_URI)
sp = spotipy.Spotify(auth_manager=token)

# new music to add to playlist
new_tracks = []
# old music to delete
old_tracks = []
#music i liked from new music
liked_tracks = []
#current from my playlist
current_tracks  = []

duplicates_tracks = []




## Get existing playlist and add 
def grabUri(picked_playlist):
    results = sp.user_playlist_tracks(user=username,playlist_id=picked_playlist)
    tracks = results["items"]
    print(results["next"])
    
    if results["next"]:
        while results["next"]:
            results = sp.next(results)
            tracks.extend(results["items"])
            for i in range(len(tracks)):
                new_tracks.append(tracks[i]["track"]["uri"])
            break
    else:
         for i in range(len(tracks)):
                new_tracks.append(tracks[i]["track"]["uri"])
        
        


    
def new_music_added():
    grabUri(rnb_kpop)
    grabUri(new_music_kpop)
    delete_old_tracks(new_tracks)
    
    print(len(new_tracks))
    if len(new_tracks) != 0: 
    
        add_to_playlist(new_music_playlist,new_tracks)

def delete_old_tracks(tracks):
        while tracks:
            sp.user_playlist_remove_all_occurrences_of_tracks(user=username,playlist_id=new_music_playlist,tracks=tracks[:100])
            tracks = tracks[100:]
    


def update_myplaylist():
    
    try:
        saved_tracks = sp.current_user_saved_tracks()
        for i in range(len(saved_tracks["items"])):
            liked_tracks.append(saved_tracks["items"][i]["track"]["uri"])
        
        current_playlist =sp.user_playlist_tracks(user=username,playlist_id=playlist_id)
        for i in range(len(current_playlist["items"])):
            current_tracks.append(current_playlist["items"][i]["track"]["uri"])
   
        
        duplicates = list(set(liked_tracks).intersection(set(current_tracks)))
        no_dupes = list(set(current_tracks).symmetric_difference(liked_tracks))
        print(no_dupes)
       
        
        print(liked_tracks)
        
        if len(duplicates) != 0:
            sp.current_user_saved_tracks_delete(tracks=duplicates)
            updated_tracks = sp.current_user_saved_tracks()
            no_dupes = list(set(current_tracks).symmetric_difference(liked_tracks))
            print(no_dupes)
            list.clear(no_dupes)
            liked_tracks.append(no_dupes)
        if len(liked_tracks) != 0:
            add_to_playlist(playlist_id,liked_tracks)
            sp.current_user_saved_tracks_delete(tracks=liked_tracks)
    except:
        print("no liked songs added")

def add_to_playlist(playlist,tracks):
    while tracks:
        print("asdffdsafdsafdsa")
        sp.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=tracks[:100])
        tracks = tracks[100:]
   
         
        
        
    

new_music_added()
update_myplaylist()



    
    

 
    




    

    


    
 







