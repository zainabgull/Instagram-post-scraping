from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

driver = webdriver.Firefox() #NOTE: FIREFOX EXAMPLE
driver.get("http://www.instagram.com")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))

password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
username.send_keys("Username")

password.clear()
password.send_keys("[password]")

Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
try:
    # Handle the first "Not Now" button
    alert = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))
    )
    alert.click()
except Exception as e:
    print("First 'Not Now' button not found or could not be clicked.")

try:
    # Handle the second "Not Now" button
    alert2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))
    )
    alert2.click()
except Exception as e:
    print("Second 'Not Now' button not found or could not be clicked.")
import time

#target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

#search for the hashtag cat
keyword = "#hiast"
searchbox.send_keys(keyword)
 
# Wait for 5 seconds
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)


driver.execute_script("window.scrollTo(0,4000);")

images = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
images=[image.get_attribute('src') for image in images]


path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")
path
os.mkdir(path)
counter = 0
for image in images:
    try:
        save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1
    except Exception as e:
        print(f"Error downloading image {image}: {str(e)}")

driver.quit()