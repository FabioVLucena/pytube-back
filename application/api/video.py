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
    
    response = Response(videoListJson, mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@video.route('/download/<uuid>')
def downloadSongByUrl(uuid):
    url = 'https://www.youtube.com/watch?' + uuid
    
    yt = YouTube(url)
    audio = yt.streams.get_audio_only()
    file_path = audio.download(output_path="../downloads")
    
    with open(file_path, 'rb') as video_file:
        response = Response(video_file.read(), mimetype='audio/mp3')

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

