from pydantic import BaseModel
from pydantic.dataclasses import dataclass

@dataclass
class Video(BaseModel):
    title: str
    video_url: str
    thumbnail_url: str

    def __init__(self, title: str, video_url: str, thumbnail_url: str) -> None:
        super().__init__(title=title, video_url=video_url, thumbnail_url=thumbnail_url)