from pytube import Playlist

playlist = Playlist("https://www.youtube.com/watch?v=zmxJbz-o-Ak&list=PLT9lZaywI5etSYh7EqkeKB0E_8cqTN1w_");
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.videos :
    video.streams.get_audio_only().download(output_path="./videos")