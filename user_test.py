import unittest 
import pyperclip
from user import User


class TestUser(unittest.TestCase):
    '''
      shows the test cases for the user class
    
    '''
    def setUp(self):
        '''
        shows the format or method that should run before each test
        '''
        self.new_user = User("Kennedy","Mbithi","Mutia2001")
    def test_init(self):
        '''
         checks if the object is initialised properly using the init command
        '''
        self.assertEqual(self.new_user.first_name,"Kennedy")
        self.assertEqual(self.new_user.second_name,"Mbithi")
        self.assertEqual(self.new_user.password,"Mutia2001")
    def test_save_user(self):
        '''
         checks if the new user created is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),3)

    def test_save_multiple_user(self):
        '''
         checks if it can allow many user instances to be created at the same time
        '''
        self.new_user.save_user()
        test_user = User("tests","users","ken")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_display_users(self):
        '''
         displays all users that have registered or signed
        '''
        self.assertEqual(User.display_users(),User.user_list)
    def test_user_exist(self):
        '''
        checks if a user is in the list
        '''
        self.new_user.save_user()
        test_user = User("tests","sickname","password")
        test_user.save_user()
        user_exists =User.user_exist("test")
    

        self.assertTrue(user_exists)
if __name__ == '__main__':
    unittest.main()
