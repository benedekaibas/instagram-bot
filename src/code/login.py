"""Login for the user's Instagram profile."""

import instaloader
from rich.console import Console
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
        self.download_location = "src/code/pictures"

        answer = str(input("Do you want to download pictures and videos from instagram (y/n): "))
        if answer.lower() == 'y':
            for picture in pictures:
                self.loader.download_post(picture, target = self.username)
