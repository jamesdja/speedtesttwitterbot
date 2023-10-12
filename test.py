import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PYTHON_LINK = "https://twitter.com/i/flow/login"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(PYTHON_LINK)
time.sleep(5)
first_name = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
first_name.send_keys("jamesdjajadi@gmail.com")

time.sleep(1)

login = driver.find_element(By.CSS_SELECTOR, "div[class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu']")
login.click()

time.sleep(3)

phone_number = driver.find_element(By.CSS_SELECTOR, 'input[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
phone_number.send_keys("jamessdja")

time.sleep(1)

next = driver.find_element(By.CSS_SELECTOR, "div[class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr']")
next.click()

time.sleep(3)

password = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
password.send_keys("Jakarta12196#")

time.sleep(1)
#
final_login = driver.find_element(By.CSS_SELECTOR, "div[class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr']")
final_login.click()

time.sleep(3)

password = driver.find_element(By.CSS_SELECTOR, 'div[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
password.send_keys("Hello World")

post = driver.find_element(By.CSS_SELECTOR, "div[class='css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']")
post.click()
# last_name = driver.find_element(By.XPATH, "/html/body/form/input[2]")
# last_name.send_keys("Newton")
#
# last_name = driver.find_element(By.XPATH, "/html/body/form/input[3]")
# last_name.send_keys("jn@noob.com")
#
# button= driver.find_element(By.XPATH, "/html/body/form/button")
# button.click()
