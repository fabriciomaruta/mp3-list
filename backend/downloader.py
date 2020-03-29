import os
from flask import Flask
from flask_restful import Resource

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEV_KEY = 'AIzaSyAo1e866tzIGdMUvyDcP7VF_ZkEQ9Hw2pY'
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class Downloader(Resource):
	def get(self):
		result = youtube_search()
		formatedUrls = []
		for videos in result :
			url = 'youtube.com/watch?v=' + videos['id']
			formatedUrls.append(url)
		download_from_youtube(formatedUrls[0])
		return{'data': 'SUCCESS','formatted urls': formatedUrls, 'raw': result }


def download_from_youtube(video_url):
	os.system("youtube-dl -x --audio-format mp3 " + video_url)

def youtube_search():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEV_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q='essa tal liberdade',
    part="id,snippet",
    maxResults=3
  ).execute()
  
  videos = []
  
  

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
    	video = {}
    	video['title'] = search_result["snippet"]["title"]
    	video['id'] = search_result["id"]["videoId"] 
    	videos.append(video)
    		
  return (videos)