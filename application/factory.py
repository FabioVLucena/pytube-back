from flask import Flask
from application.api.video import video

def create_app():
    app = Flask(__name__)
    app.register_blueprint(video, url_prefix=video.url_prefix)

    return app