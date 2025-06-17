



from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# start Selenium session 
driver = webdriver.Chrome()


# action so here navigate to a web page

driver.get("https://www.youtube.com/watch?v=YltjliK0ZeA&list=RDYltjliK0ZeA&index=2")

# now request browser information


title = driver.title


# sync state with the current browser

driver.implicitly_wait(5)

# find an element 
#play button
play_button = driver.find_element(By.CLASS_NAME, "ytp-play-button")
# accept the cookies button

#function to check for cookies and also accept it automatically
def click_away_cookies():
    
    try:
    #i used the f12 conmsole to find out the exact path of the accept button that will remove the cookie accept window
        cookies_accept_button = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button')
        time.sleep(4)
        cookies_accept_button.click()
        time.sleep(4)  
        print("Cookies akyeptiert!")
   
    
    except:
        print("cookies fenster nicht entdeckt")
time.sleep(3)
click_away_cookies()

#function to find the adds i will later then try to remove or cover up
def find_Adds():
    ad_div_visible = 0
    add_video = None
    
    try: 
        add_video = driver.find_element(By.CLASS_NAME, "video-ads")
        print(add_video)
        print("adds found and probably playing!")
        ad_div_visible =1
    
    except:
        print("couldnt find adds")

    return [add_video, ad_div_visible]

adds = find_Adds()
# conditions or values i need for the Model
ad_visible = find_Adds()
isDisplayed = 0


# for my Model i need features to detect what kind of adds are going so i try to get button text or any texts inside the add for classification


def extract_text_for_classification():
    context = []

    try: 
        context = driver.find_element(By.CLASS_NAME, "ytp-ad-overlay-layout__ad-info-container", "ytp-ad-overlay-layout__player-card-container")

    except:
        False


    return context




ad_context_overlay_text_model_feature = extract_text_for_classification()








#function to remove the adds if we found some

def remove_adds(adds):
    #TODO create function to remove adds
    pass

# search for elements 
#elements = driver.find_elements(By.TAG_NAME, "button")

#for e in elements:
#    print(e.text)


# take action on an element
#





# finally end the session

#wait for user input so it wont quit after finishing all the code i need it be open more longer

input("enter something to quit the session")

# to close the session driver.quit()


#TODO find the exath path for the adds to later turn them of
