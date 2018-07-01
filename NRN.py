import json
import requests


userName = input("User Name: ")
password = input("Password: ")
serverName = input("Server Name: ")

from plexapi.myplex import MyPlexAccount
account = MyPlexAccount(userName, password)
plex = account.resource(serverName).connect()

library = plex.library.section('Movies')
print(library.recentlyAdded(3))
