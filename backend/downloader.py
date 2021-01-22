from flask import Flask
from flask_restful import Resource, Api
import youtube_dl

class Downloader(Resource):
    def get(selfi, video_id):
        url = 'https://www.youtube.com/watch?v=' + video_id
        download_video(url)
        return {'message':'downloaded it, enjoy :P'}
        
def download_video(video_url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
