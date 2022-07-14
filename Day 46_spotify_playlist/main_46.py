from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import keys

SPOTIPY_CLIENT_ID = keys.SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = keys.SPOTIPY_CLIENT_SECRET
user_s = keys.user

# Scraping Billboard 100
date = input("What year you would like to travel in YYYY-MM-DD format: ")
url_hot100 = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=url_hot100)

soup = BeautifulSoup(response.text, "html.parser")

song_names = soup.find_all("h3", id="title-of-a-story")
song_list = []

for song in song_names:
    if "Songwriter" in song.getText() or "Producer" in song.getText() or "Promotion Label" in song.getText():
        continue
    elif "Gains in Weekly" in song.getText() or "Additional Awards" in song.getText():
        continue
    else:
        song_list.append(song.getText())

song_names_100 = [str(song).strip() for song in song_list[0:100]]


# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=keys.SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

klient = sp.current_user()
# print(klient["display_name"])

# pprint.pprint(sp.current_user_playlists())
songs_ids = []

# pprint.pprint(songs_ids)
playlist = sp.user_playlist_create(user=user_s, name="Billboard 100 essa2", public=False)

for song in song_names_100:
    try:
        zwrot = sp.search(song, limit=1, type='track', market=None)
        piosenka_id = zwrot["tracks"]["items"][0]["id"]
        songs_ids.append(piosenka_id)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist["id"], items=songs_ids)