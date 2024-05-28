import bot
import clip
import download
import time

# These 2 variables are optional base on whether you want the bot to fill in your TikTok information for you or not
user = "PloTok55"
password = "Al1237497"


def main():
    
    # will ask to be login first before the bot fully runs
    bot.login("other", user, password)
    
    
    # This part will ask for the video link to be downloaded and uploaded to TikTok
    link = input("Enter the Youtube Video Link: ")
    video_title, video_duration , video_creator, channel_url = download.youtube_download(link)
    video_file = ("/" + video_title + ".mp4")
    print(video_file, video_duration)
    
    
    # the user will need the manually choose the caption and how many parts the video should have
    caption = f"Made by {video_creator} {link} #fyp #foryoupage" 
    parts = 3
    
    
    # edit the downloaded video into TikTok format
    clip.edit_video(video_file = video_file,
                    video_title = video_title, 
                    video_duration=video_duration-1, 
                    background="/A_black_background.jpg", 
                    parts=parts)


    # Have the bot automatically upload and clip the newly editted video to TikTok

    bot.upload(video_path = "/converted_video.mp4",
               video_duration = video_duration-1,
               parts_amount = parts,
               captions = caption)

if __name__ == "__main__":
    main()