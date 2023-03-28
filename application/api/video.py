from pytube import YouTube, Search
from flask import Blueprint, Response
from application.dataclass.video import Video

import json

video = Blueprint('video', __name__)
video.url_prefix = '/video'

@video.route('/search/<title>')
def searchVideoByTitle(title):
    videoList = []
    result = Search(title)
    
    for v in result.results:
        videoTitle = str(v.title)
        videoUrl = str(v.watch_url)
        videoThumb = str(v.thumbnail_url)
        video = Video(title=videoTitle, video_url=videoUrl, thumbnail_url=videoThumb)
        videoList.append(video.dict())

    videoListJson = json.dumps(videoList)

    return Response(videoListJson, mimetype='application/json')

@video.route('/download/<uuid>')
def downloadSongByUrl(uuid):
    url = 'https://www.youtube.com/watch?' + uuid
    video = YouTube(url)
    title = video.title
    return Response(json.dumps(title), mimetype='application/json')

