from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

import flickrapi

key = "93f5c6520580116ce6bc5b3e3546f74c"
secret = "0b71669e4d32bb7d"
wait_time = 1

animal_name = sys.argv[1]
savedir = "./animal/" + animal_name

flickr = FlickrAPI(key, secret, format="parsed-json")
result = flickr.photos.search(
    text = animal_name,
    per_page = 400,
    media = 'photos',
    sort = 'relevanse',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']

#返り値を表示
# pprint(photos)

for i, photo in enumerate(photos['photos']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
    
