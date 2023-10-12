from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitter:
    def __init__(self):
        self.first_name = None
        SPEEDTEST_WEBSITE = "https://www.speedtest.net/"


        self.upload_treshold = 40
        self.download_treshold = 25
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(SPEEDTEST_WEBSITE)
        self.go_button = self.driver.find_element(By.XPATH,
                                        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go_button.click()

        time.sleep(45)

        self.download = self.driver.find_element(By.XPATH,
                                       '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = float(self.download.text)

        self.upload = self.driver.find_element(By.XPATH,
                                     '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = float(self.upload.text)

    def get_internet_speed(self):
        print(f"down : {self.down}")
        print(f"up : {self.up}")

    def tweet_at_provider(self):
        X_WEBSITE = "https://twitter.com/i/flow/login"

        ID = "jamesdjajadi@gmail.com"
        PASSWORD = "Jakarta12196#"
        if self.down < self.download_treshold or self.up < self.upload_treshold:
            self.driver.get(X_WEBSITE)
            time.sleep(5)
            self.first_name = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
            self.first_name.send_keys(ID)

            time.sleep(1)

            self.login = self.driver.find_element(By.CSS_SELECTOR,
                                        "div[class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu']")
            self.login.click()

            time.sleep(3)

            self.phone_number = self.driver.find_element(By.CSS_SELECTOR,
                                               'input[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
            self.phone_number.send_keys("jamessdja")

            time.sleep(1)

            self.next = self.driver.find_element(By.CSS_SELECTOR,
                                       "div[class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr']")
            self.next.click()

            time.sleep(3)

            self.password = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
            self.password.send_keys(PASSWORD)

            time.sleep(1)
            #
            self.final_login = self.driver.find_element(By.CSS_SELECTOR,
                                              "div[class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr']")
            self.final_login.click()

            time.sleep(3)

            self.password = self.driver.find_element(By.CSS_SELECTOR,
                                           'div[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
            self.password.send_keys(f"Hey Internet Providers, my current speed is {self.down}/{self.up}, i pay for {self.download_treshold}/{self.upload_treshold}")

            self.post = self.driver.find_element(By.CSS_SELECTOR,
                                       "div[class='css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']")
            self.post.click()







