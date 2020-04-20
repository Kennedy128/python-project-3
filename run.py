#!/usr/bin/env python3.6
from user import User
import string
import random
import getpass
import pyperclip
from credentials import Credential

def create_credential(account_name,passkey):
    '''
    create a new instance of credentials
    '''
    new_credential = Credential(account_name,passkey)
    return new_credential
def save_credential(credential):
    '''
    function to save a credential
    '''
    credential.save_credential()
def display_credentials():
    '''
    function that will dispaly all the credentials
    '''
    return Credential.display_credentials()
def del_credential(credential):
    '''
    function that deletes a credential
    '''
    credential.del_credential()
def check_existing_user(password2):
    '''
    function  that enables the login authentification
    '''
    return User.user_exist(password2)
def find_account(password2):
    '''
    function to find account by the user name
    '''
    return User.find_account(password2)


def create_user(f_name,s_name,password):
    '''
    function to create a new user instance
    '''
    new_user = User(f_name,s_name,password)
    return new_user
def save_users(user):
    '''
    function to save the user
    '''
    user.save_user()
def display_users():
    '''
    function that dispalys all signed up users
    '''
    return User.display_users()
def intro():
    print("Hey there! Welcome to Passcord")
    print('\n')
    print("Please sign up to an account to get all the privileges offered")
    
    while True:
        print("⇨ Use these short codes : su - Sign up, lg - login, du-display all users, ex-Exit app ")
        print('-'*64)
        print('\n')
        short_code = input().lower()
        print('\n')
        if short_code == 'su':
            print("New User")
            print("-"*9)

            print("input you first name...")
            f_name = input()

            print("input your second name...")
            s_name=input()

            print("input your password...")
            password=input()
            print('\n')

            save_users(create_user(f_name,s_name,password))
            print('\n')
            print(f"⇨ Congratulations {f_name} {s_name}, you now have an account and you have succesfuly joined us \n")
            print('\n')
        elif short_code == 'lg':

            print("Enter the first name of your  account")
            account_name = input()
            print('\n')

            authentification = getpass.getpass('Password:')
            if check_existing_user(authentification):
                search_account = find_account(authentification)



                while True:
                    print(f"⇨ Welcome {search_account.first_name} {search_account.second_name} \n")
                    print("⇨ cc-To create new credential, vc-To view all your credentials created, ex-exit the account,dc to delete a given credential \n ")
                    print('-'*80)
                    short_code=input().lower()
                    if short_code == 'cc':
                        print("New credential")
                        print('-'*14)
                        print("Enter account name")
                        account_name = input()
                        print("Make a password \n")
                        print("To make your own password press- a, to generate a password press - g \n")
                        print('-'*50)
                        generate=input()
                        print('\n')

                        if generate == 'g':
                            letters = string.ascii_letters + string.digits
                            gpassword = ''.join(random.choice(letters) for i in range(9))
                            print(f"Your new generated password is: {gpassword} \n")
                            passkey=gpassword

                        elif generate == 'a':
                            print("Enter its password")
                            passkey = input()
                            print('\n')
                        print(f"👍_{account_name} has been saved")

                        save_credential(create_credential(account_name,passkey))

                    elif short_code == 'vc':
                        if display_credentials:
                            print("⇨ Here is a printed list of  all your accounts and passwords history \n")
                            for credential in display_credentials():
                                print(f"Account name: {credential.account_name} - password: {credential.passwordkey}")
                    elif short_code == 'dc':
                        print("Which credential would you like to delete?")
                        del_account = input()
                        if del_account == account_name:

                            Credential.credential_list.remove(credential)
                            print("👍_Credential deleted")
                        else:
                            print("No match of the credential inputed")

                    elif short_code == 'ex':
                        print("You have executed your account \n")
                        break
            else:
                print("The password you inputed was not a match \n")
                print('\n')
        elif short_code == 'du':
            print("Here is a displayed list of all the users\n")
            for user in display_users():
                print(f"{user.first_name} {user.second_name} \n")

        elif short_code == 'ex':

            print("pleasue. it was nice working with you! \n")

            break
        else:
            print("☹ _ I dont get that, please use these codes \n")

if __name__ == '__main__':

    intro()
