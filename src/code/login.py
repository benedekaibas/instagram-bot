"""Login for the user's Instagram profile."""

import time
import sys, os, glob, shutil
import instaloader
from rich.console import Console
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver import ActionChains


"""
username: bet3655416
password: Pythonproba99-
"""

console = Console()


class Login:
    """Class containing the needed functions."""

    def __init__(self, username, password, download_location):
        self.username = username
        self.password = password
        self.loader = instaloader.Instaloader()
        self.download_location = download_location

    def user_login_information(self):
        """Do the login based on user's information."""

        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")

        return self.username, self.password
    
    def user_login(self):
        """Checking user's followers."""
        return self.loader.login(self.username, self.password)
    
    def check_followers(self):
        """Checking the followers of the given user."""

        for follower in instaloader.Profile.from_username(self.loader.context, self.username).get_followers():
            console.print(follower)
        return follower

    def check_followee(self):
        """Checking the followees of the given user."""
        for followee in instaloader.Profile.from_username(self.loader.context, self.username).get_followees():
            console.print(followee)
        return followee

    def count_information(self):
        """Counting followers and followees."""
        followers = str(self.check_followers())
        followees = str(self.check_followee())
        console.print(f"You have {len(followers)} followers.")
        console.print(f"You have {len(followees)} followees.")

    def download_picture(self):
        """Posting a selected picture from the computer using the bot."""
        pictures = instaloader.Profile.from_username(self.loader.context, self.username).get_posts()
        self.download_location = "/Users/benedekkaibas/Desktop/instagram-bot/src/code/pictures"
        if os.path.exists(self.download_location):
            console.print("Path does exist")
        else:
            console.print("Path does not exist")
        answer = str(input("Do you want to download pictures and videos from instagram (y/n): "))
        if answer.lower() == 'y':
            for picture in pictures:
                self.loader.download_post(picture, target=self.username)
                files = glob.glob(os.path.join(self.username, '*'))
                for file in files:
                    shutil.move(file, self.download_location)
    
    def remove_folder(self):
        """Remove folder that is not needed after content have been downloaded from Instagram."""
        return shutil.rmtree(self.username)

class InstaBot():
    """Bot for interacting with the Instagram website."""

    def __init__(self):
        """Using the selenium library for the code and storing it."""
        self.username = os.environ.get('USERNAME')
        self.password = os.environ.get('PASSWORD')
        self.url = "https://www.instagram.com/"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 5)

    def bot_login(self):
        """Login method for the bot."""
        self.browser.get(self.url)

        try:
            cookies = self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Allow all cookies"]')))
            cookies.click()
        except Exception as e:
            print(f"Error while closing cookies window: {e}")

        ig_username = self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        ig_password = self.wait.until(EC.presence_of_element_located((By.NAME, 'password')))

        ig_username.send_keys('bet3655416')
        ig_password.send_keys('Pythonproba99-')
        ig_password.send_keys(Keys.ENTER)

        time.sleep(5)

        try:
            save_login = self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Save info"]')))
            save_login.click()
        except Exception as e:
            print(f"Error while closing save login window: {e}")

        time.sleep(5)

        try:
            notifications = self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now"]')))
            notifications.click()
        except Exception as e:
            print(f"Error while closing notifications tab: {e}")

        time.sleep(5)

    def scroll(self):
        """Automated script for scrolling through the website."""
        time.sleep(5)
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for the new content to load
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:  # If the new height is the same as the old height, we've reached the bottom
                break
            last_height = new_height


# we call instabot here only for test after that we have to call it from the main file.
if __name__ == "__main__":
    insta_bot = InstaBot()
    insta_bot.bot_login()
    insta_bot.scroll()
