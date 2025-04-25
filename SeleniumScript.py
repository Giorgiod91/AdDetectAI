



from selenium.webdriver.common.by import By
from selenium import webdriver

# start Selenium session 
driver = webdriver.Chrome()


# action so here navigate to a web page

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# now request browser information


title = driver.title


# sync state with the current browser

driver.implicitly_wait(0.5)



# find an element 
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")


# take action on an element

text_box.send_keys("Selenium")
submit_button.click()


# request element information

message = driver.find_element(by=By.ID, value="message")
text = message.text

print(text)


# finally end the session

driver.quit()



