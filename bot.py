from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import os
import time


    # contents for Tik Tok's upload page are within an IFrame so we must switch into that
    # IFrame to interact with those elements
def jump_to_iframe(driver):
    iframe_path = '//*[@id="root"]/div[2]/div[2]/div/div/iframe'
    try:
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, iframe_path))
        )
    except:
        print("Failed To Find Iframe")
        driver.quit()
        quit()

    iframe = driver.find_element(By.XPATH, iframe_path)
    driver.switch_to.frame(iframe)
    return


    # This function sets up the driver that will be used for botting
def set_up_driver():
    
    options = uc.ChromeOptions()
    
    # each user will have separate chrome profile path 
    # you find it by searching up the url 'chrome://version/' next to profile path
    chrome_profile_path = r'C:\Users\Boao\AppData\Local\Google\Chrome\User Data\Default'
    
    # the options.add_argument allows the driver to save its session
    options.add_argument(fr'--user-data-dir={chrome_profile_path}')
    driver = uc.Chrome(options = options)
    
    return driver


# This function will have the user manually login and solve captcha and to make sure the user is logged in before botting
def login(option, user_email_username="", user_pw=""):
    
    print("This Process Requires the User to Manually Login or Verify Captcha Based On The Options Chosen")
    time.sleep(5)
    
    driver = set_up_driver()
    
    driver.get("https://www.tiktok.com/upload?lang=en")

    login_page = '//*[@id="login-modal-title"]'
    login_option = '//*[@id="loginContainer"]/div/div/div/div[3]/div/p'
    upload_page = '//*[@id="root"]/div/div/div/div/div/div/div/div'
    
    
    # checks whether we are already logged in or not
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, login_page))
        )
    except:
        print("Already Logged in")
        driver.quit()
        return
    
    
    # if the option is to login through TikTok login then the bot with fill out the login info for the user
    if option == "other":
        # select the option to login via tik tok login and not email login
        login = driver.find_element(By.XPATH, login_option)
        login.click()
        
        
        # will select on the options to login via email instead of phone number
        select_other_option = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/a')
        select_other_option.click()
        
        
        # find the input form for taking in email and password then auto type out the login information before submitting
        login_input = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/input')
        login_input.send_keys(user_email_username + Keys.TAB + user_pw + Keys.ENTER)
        
        # will give the bot 30 seconds to wait to see if we have successfully logged in or not
    
    else:
        print("The User will be given 5 min to try to manually log in through email")
        time.sleep(300)
    
    # if the option is through email, the user is given 5 min to manually log in
    
    
    # final check to see if we have logged in successfully or not
    jump_to_iframe(driver)
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, upload_page))
        )
        print("Login Success")
        return 
    
    except:
        print("Login Failed")
        return
    



# this function will perform the main task of auto clipping and uploading to TikTok
def upload(video_path, video_duration, parts_amount, captions):
    
    # To combine the video file location with the video mp4 file
    video_path = os.path.dirname(__file__) + video_path
    
    driver = set_up_driver()
    driver.get("https://www.tiktok.com/upload/?lang=en")


    upload_input = '//*[@id="root"]/div/div/div/div/div/div/div/input'
    
    jump_to_iframe(driver)
    
    # checks to see if we are within the upload page and if not the program stops as user are not logged in
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, upload_input))
        )
    except:
        print("Login Failed")
        driver.quit()
        quit()
    
    file_input = driver.find_element(By.XPATH, upload_input)
    file_input.send_keys(video_path)
    
    
    # there will be different options given depending on the video length so this if statement ensures that
    # The bot clicks on the right element depending on the video duration
    
    if video_duration >= 600:
        
        edit_option_path = '//*[@id="tux-portal-container"]/div[2]/div/div/div/div/div[2]/div/div/button[1]/div/div'
        # will give it time to load the video and wait for Tik Tok to ask for the option to edit
        # If after 2 minute that the video doesn't load or no option for edit then it will print out        
        try:
            WebDriverWait(driver, 120).until(
                EC.presence_of_all_elements_located((By.XPATH, edit_option_path))
            )
        except:
            print("Edit Option Element Not Found")
            
        edit = driver.find_element(By.XPATH, edit_option_path)
        edit.click()
        
        
        cancel_path = '//*[@id="tux-portal-container"]/div[2]/div/div/div/div/div[2]/div/div[1]/span/div/div[2]/button[1]/div/div'
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, cancel_path))
            )
        except:
            print("Cancel Element Not Found")
        
        cancel = driver.find_element(By.XPATH, cancel_path)
        cancel.click()  
    
    
    
    # After clipping video, the bot will then add the captions the user inputted
    caption_path = '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div'
    
    try:
        WebDriverWait(driver, 120).until(
            EC.presence_of_all_elements_located((By.XPATH, caption_path))
        )
    except:
        print("Failed To Find Caption Element")

    # Act as select all and delete
    caption = driver.find_element(By.XPATH, caption_path)
    caption.send_keys("Sel")
    caption.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    time.sleep(2)
    caption.send_keys(captions)
    time.sleep(2)

    
    # wait for the split element to appear before we have the bot access and use it
    split_path = '//*[@id="root"]/div/div/div/div[1]/div[2]/div[2]/button'
    split_amount_path = '//*[@id="root"]/div/div/div/div[1]/div[2]/div[1]/div/span[2]/input'
    
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, split_amount_path))
        )
    except:
        print("Failed to Find Split Element")
    
    split_amount = driver.find_element(By.XPATH, split_amount_path)
    time.sleep(1)
    split_amount.clear()
    split_amount.send_keys(parts_amount)
    split = driver.find_element(By.XPATH, split_path)
    split.click()
    
    
    # Wait for the save video option before we save our edit
    time.sleep(5)
    
    save_edit_path = '//*[@id="tux-portal-container"]/div[2]/div/div/div/div/div[2]/div/div[1]/span/div/div[2]/button[2]'
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, save_edit_path))
        )
    except:
        print("Failed To Find Save Video")
    
    save_video = driver.find_element(By.XPATH, save_edit_path)
    save_video.click()
    
    
    time.sleep(5)
    
    
    # wait for the post option to load before having the bot post the video
    post_path = '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[8]/div[2]/button'
    
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, post_path))
        )
    except:
        print("Failed To Find Post Element")

    post = driver.find_element(By.XPATH, post_path)
    post.click()
    
    
    print("Done")
    time.sleep(10)
    driver.quit()



        
if __name__ == '__main__':
    # login("email", "PloTok55", "Al1237497")

    upload(video_path = "/converted_video.mp4",
               video_duration = 568,
               parts_amount = 3,
               captions = "Made by Kurokori https://www.youtube.com/watch?v=pffBBTgEcxw #fyp #foryoupage")

