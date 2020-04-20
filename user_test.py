import unittest #unnitest module import
import pyperclip
from user import User


class TestUser(unittest.TestCase):
    '''
      defines the test cases for user class
    
    '''
    def setUp(self):
        '''
        Setup method to run before each test cases
        '''
        self.new_user = User("Kennedy","Mbithi","Mutia2001")
    def test_init(self):
        '''
         checks if the object is initialised properly
        '''
        self.assertEqual(self.new_user.first_name,"Adrian")
        self.assertEqual(self.new_user.second_name,"Etenyi")
        self.assertEqual(self.new_user.password,"Mutemuas2001")
    def test_save_user(self):
        '''
         tests if a new user created is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),3)

    def test_save_multiple_user(self):
        '''
         tests if many users can be saved at the same time
        '''
        self.new_user.save_user()
        test_user = User("tests","users","ken")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_display_users(self):
        '''
         displays all thes signed  users
        '''
        self.assertEqual(User.display_users(),User.user_list)
    def test_user_exist(self):
        '''
        test to check if a user exists in the list
        '''
        self.new_user.save_user()
        test_user = User("tests","sickname","password")
        test_user.save_user()
        user_exists =User.user_exist("test")
    

        self.assertTrue(user_exists)
if __name__ == '__main__':
    unittest.main()
