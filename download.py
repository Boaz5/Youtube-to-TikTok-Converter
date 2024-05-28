
from pytube import YouTube


def youtube_download(link):
    video = YouTube(link)

    print(f"Thumbnail Image: {video.thumbnail_url}")
    
    video_duration = video.length
    video_title = video.title
    video_creator = video.author
    channel_url = video.channel_url
    
    video_title = "".join(char for char in video_title if char not in '?:"|')
    
    video = video.streams.get_highest_resolution()

    video.download(filename=video_title + ".mp4")
    
    return (video_title, video_duration, video_creator, channel_url)


if __name__=='__main__':
    print("Download.py")
    youtube_download("What Ever Youtube Video Link")