



from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# start Selenium session 
driver = webdriver.Chrome()


# action so here navigate to a web page

driver.get("https://www.youtube.com/watch?v=A-jQRB-r2Do&list=RDA-jQRB-r2Do&start_radio=1")

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
    
        cookies_accept_button.click()
        time.sleep(2)  
        print("Cookies akyeptiert!")
   
    
    except:
        print("cookies fenster nicht entdeckt")



#function to find the adds i will later then try to remove or cover up
def find_Adds():
    ad_div_visible = 0
    
    try: 
        add_video = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div[2]/ytd-player/div/div/div[7]")
        print(add_video)
        print("adds found !")
        ad_div_visible =1
    
    except:
        print("couldnt find adds")

    return [add_video, ad_div_visible]

adds = find_Adds()

ad_visible = find_Adds()



#function to remove the adds if we found some

def remove_adds(adds):
    #TODO create function to remove adds

# search for elements 
elements = driver.find_elements(By.TAG_NAME, "button")

#for e in elements:
#    print(e.text)


# take action on an element
#

# define values that i will use in my model later on
value_x = 0



# finally end the session

#wait for user input so it wont quit after finishing all the code i need it be open more longer

input("enter something to quit the session")

driver.quit()


#TODO find the exath path for the adds to later turn them of
