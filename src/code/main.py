"""Main file for calling classes from other files."""

from login import Login
from rich.console import Console

console = Console()

class Main:
    def __init__(self):
        pass
    
    def run(self):
        login = Login('', '', '')
        login.user_login_information()
        login.user_login()
        login.check_followers()
        console.print("")
        login.check_followee()
        console.print("")
        login.count_information()
        login.download_picture()
        if login.answer.lower() == 'y':
            login.remove_folder()
        login.call_mutuals()


if __name__ == "__main__":
    main = Main()
    main.run()