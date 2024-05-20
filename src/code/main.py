"""Main file for calling classes from other files."""

from login import Login

class Main:
    def __init__(self):
        pass
    
    def run(self):
        login = Login('', '')
        login.user_login_information()
        login.user_login()
        login.check_followers()
    


if __name__ == "__main__":
    main = Main()
    main.run()
