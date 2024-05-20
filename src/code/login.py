"""Login for the user's Instagram profile."""

import instaloader

class Login:
    """Class containing the needed functions."""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.loader = instaloader.Instaloader()

    def user_login(self):
        """Do the login based on user's information."""

        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")

        return self.username, self.password
    
    def check_followers(self):
        """Checking user's followers."""
        return self.loader.login(self.username, self.password)