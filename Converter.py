import yt_dlp as youtube_dl
import os
def convert_music_from_yt(url):
    output_dir = 'songs'
    ydl_opts = {
        'format': 'bestaudio/best', 'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s', ), 'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',}],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        path = ydl.prepare_filename(info)
