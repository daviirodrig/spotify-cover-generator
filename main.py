import logging
import os

import dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

import gen_img

dotenv.load_dotenv()
sp = Spotify(
    oauth_manager=SpotifyOAuth(
        scope="ugc-image-upload,playlist-modify-public,playlist-modify-private"
    )
)

playlist_id = os.environ['PLAYLIST_ID']

img_str = gen_img.execute(3000, playlist_id)



res = sp.playlist_upload_cover_image(playlist_id, img_str)
#print(res)
