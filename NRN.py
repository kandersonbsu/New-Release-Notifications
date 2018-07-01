import json
import requests


userName = input("User Name: ")
password = input("Password: ")
serverName = input("Server Name: ")
from plexapi.myplex import MyPlexAccount
account = MyPlexAccount(userName, password)
plex = account.resource(serverName).connect()

movies = plex.library.section('Movies')
for video in movies.search(unwatched=True):
    print(video.title)