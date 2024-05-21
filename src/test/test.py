"""Unittest for the project"""

import unittest
from unittest.mock import patch, MagicMock
from code.login import Login

class TestLogin(unittest.TestCase):
    """Unittest for the login.py file."""

    @patch('login.instaloader')
    def setUp(self, mock_instaloader):
        self.mock_instaloader = mock_instaloader
        self.login = Login('test_username', 'test_password')

    @patch('builtins.input', side_effect=['test_username', 'test_password'])
    def test_user_login_information(self, mock_input):
        username, password = self.login.user_login_information()
        self.assertEqual(username, 'test_username')
        self.assertEqual(password, 'test_password')

    def test_user_login(self):
        self.login.user_login()
        self.mock_instaloader.Instaloader().login.assert_called_once_with('test_username', 'test_password')

    @patch('login.Console')
    def test_check_followers(self, mock_console):
        mock_profile = MagicMock()
        self.mock_instaloader.Profile.from_username.return_value = mock_profile
        mock_profile.get_followers.return_value = ['follower1', 'follower2']
        self.login.check_followers()
        mock_console().print.assert_any_call('follower1')
        mock_console().print.assert_any_call('follower2')

    @patch('login.Console')
    def test_check_followee(self, mock_console):
        mock_profile = MagicMock()
        self.mock_instaloader.Profile.from_username.return_value = mock_profile
        mock_profile.get_followees.return_value = ['followee1', 'followee2']
        self.login.check_followee()
        mock_console().print.assert_any_call('followee1')
        mock_console().print.assert_any_call('followee2')

if __name__ == '__main__':
    unittest.main()
