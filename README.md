# Tik-Tok-AutoUpload-Project

* will be developed with the sole purpose of gaining coding experience and helping a friend promote his YouTube videos over TikTok so probably won't be maintained
* There's a high chance that the uploading part of the code might break over time if TikTok changes its HTML format since I'm not using TikTok's API (Since using TikTok's API for upload requires applying and being accepted for their API usage)

The goal for this project is to automatically download a YouTube video edit it with captions and upload it to TikTok
- Install the dependencies used in this project (pip install etc)
- Set up Selenium and its web drivers (use Chrome as I'm using undetected Chromedriver to avoid being detected botting on TikTok and there are many videos on Youtube on how to set up Selenium)
- The program does require the user to manually login so it's optional whether to put in your login information since all it does is have the bot type in the login information for you and you still need to do the captcha by yourself
- For the function 'edit_video' it requires an argument for a background so download any background jpeg and have it in the same folder as the program (In my case, I have "/A_black_background.jpg")
- To change how many parts you want the video to be posted in just change the "parts" variable for the amounts you want
- You can change the captions variables to fit what you want to say for the TikTok captions(In my case, I just made it so it's a Link to the creator's video with common tags like #fyp

Now, you can run 'Python run.py' and will be prompted to type in a YouTube Link. In some cases, 
the upload bot might bug out after the video has finished being downloaded and edited. In that case,
I've always had the edited video file called 'converted_video.mp4' so just run 'bot.py' after changing up
the function arguments' caption and bot to fit your preference so it'll skip the original 2 processes of downloading
and editing the video
