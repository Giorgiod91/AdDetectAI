



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
cookies_accept_button = driver.find_element(By.XPATH, '//button[contains(text(), "Alle akzeptieren") or contains(text(), "Ich stimme zu")]')
cookies_accept_button.click()
# search for elements 
elements = driver.find_elements(By.TAG_NAME, "button")

for e in elements:
    print(e.text)


# take action on an element
#
play_button.click()
time.sleep(2)
play_button.click()
# define values that i will use in my model later on
value_x = 0



# finally end the session

#wait for user input so it wont quit after finishing all the code i need it be open more longer

input("enter something to quit the session")

driver.quit()



