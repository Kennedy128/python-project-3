#!/usr/bin/env python3.6
from credentials import Credential
class User: 
    '''
    class that generates new instances of users accounts
    '''
    user_list = []
    def save_user(self):
        '''
         saves users
        '''
        User.user_list.append(self)
    def __init__(self,first_name,second_name,password):

       

        self.first_name = first_name
        self.second_name = second_name
        self.password = password
    
    @classmethod
    def display_users(cls):
        '''
        it display all the users
        '''
        return cls.user_list
    @classmethod
    def user_exist(cls,password):
        '''
        checks if user and their respective details exist
        '''
        for user in cls.user_list:
            if  user.password == password:
                return True
        return False
    @classmethod
    def find_account(cls,password2):
        '''
         finds an account by its name
        '''
        for user in cls.user_list:
            if user.password == password2:
                return user
