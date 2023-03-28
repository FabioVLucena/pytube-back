from flask import Flask
from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# stream = yt.streams.get_audio_only()
teste = yt.watch_url
print(teste)

# stream.download(output_path="./videos")