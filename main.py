import spotipy
from spotipy.oauth2 import SpotifyOAuth
scope = "user-library-read"
urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

artist = sp.artist(urn)
print(artist)

user = sp.user('plamere')
print(user)