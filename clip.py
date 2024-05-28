from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip, concatenate_videoclips
import os

# This function creates the background for the video clips
def generate_background_text(clip, message, duration, part = None):
    
    # add a newline for every 25th char for formatting purposes
    message = '\n'.join([message[i : i + 25 ] for  i in range(0, len(message), 25)])
    
    # add the title and the parts within the background
    text = TextClip(message, fontsize= 65, color = 'white')
    text2 = TextClip(f"Part {part}", fontsize= 65, color='white')
    text = text.set_position(("center", text.h + 200)).set_duration(duration)
    text2 = text2.set_position(("center", text.h + 1300)).set_duration(duration)
    clip = CompositeVideoClip([clip, text2, text])
    text.close()
    text2.close()
    return clip


# the main function for the editing of the video
def edit_video(video_file, video_title, video_duration, background, parts):
    # normal is width: 1280      height: 720

    video_file = VideoFileClip(os.path.dirname(__file__)+ video_file)

    background = VideoFileClip(os.path.dirname(__file__)+ background,
                                has_mask=True,
                                target_resolution=(1920,video_file.w))
    
    count = 0
    clip_duration = round(video_duration / parts)

    clips = []
    
    # Separates the downloaded video into clips and adding in the background 
    for i in range(0, video_duration, clip_duration):
        count+=1
        if (i + clip_duration > video_duration):
            clip_duration = video_duration - i
            print(i + clip_duration)
            print(video_duration)

        start = i
        end = i + clip_duration

        print(end)
        
        clip = video_file.subclip(start, end)
        background_video = generate_background_text(background, video_title, clip_duration, count)
        final_clip = CompositeVideoClip([background_video, clip.set_position("center")])
        
        # appends the edited clips into a list
        clips.append(final_clip)
    
    
    # combine the clips into a video
    final_vid = concatenate_videoclips(clips)
    
    final_vid.write_videofile(
        os.path.dirname(__file__) + f"/converted_video.mp4",
        fps = 24,
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
        threads = 6)
    
    final_vid.close()



if __name__=="__main__": 
    edit_video("/test.mp4", "/A_black_background.jpg", 6)