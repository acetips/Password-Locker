#!/usr/bin/env python3.8

from locker import User
from locker import Credentials

def create_passwordlocker_account(first_name,last_name,username,mypassword):
    '''
    A function for creating a user account for storing credentials
    '''
    new_user = User(first_name,last_name,username,mypassword)
    return new_user

def save_user(user):
    '''
    A function to save new user account details
    '''
    user.save_user()

def verify_user(username):
    '''
    A function to check whether the user exists
    '''
    return User.user_exists(username)

def save_credentials(credential):
    '''
    A function to save new credentials of the user
    '''
    credential.save_credentials()

def delete_credentials(credential):
    '''
    a function for deleting the saved credentials of the user
    '''
    credential.delete_credentials()

def find_credentials(website_username):
    '''
    A function to enable the user to find his or her credential
    '''
    return Credentials.find_by_website(website_username)

def show_all_credentials():
    '''
    A function to display all the user's credentials
    '''
    return Credentials.display_credentials()

def main():
    print ("Welcome to password locker. What's your name?")
    name = input()
    print(f"Greetings {name}!, Would you like to create an account or login to your existing account?")
    print('\n')
    while True:
        print("To create an account, use 'ca';To login to your account, use 'la';To exit the program, use 'ex'")
        user_input = input().lower()
        if user_input == 'ca':
            print ("Create an account")
            print("*"*6)
            print("First Name:")
            first_name = input()
            print("Last Name:")
            last_name = input()
            print("Preferred username:")
            username = input()
            print("Preferred password:")
            mypassword = input()
        elif user_input == 'la':
            print ("Login to your account")
            print("*"*6)
            print("Enter your username:")
            username = input()
            print("Enter your password")
            mypassword = input()

            save_user(create_passwordlocker_account(first_name,last_name,username,password))
            print('\n')
            print("Congratulations!Your account has been created successfully. Here are your details:")
            print(f"Account details {first_name} {last_name} {username} {password}")
            print('\n')

        elif user_input == 'la':
            print("Account login")
            print("*"*6)
            print("Username:")
            username = input()
            print("Enter your password:")
            mypassword = input()
            print('\n')
        
        elif user_input == 'ex':
            print("We are sad to see you go:(.")
            break
        
        else:
            print("Invalid user entry. kindly re-enter a valid command")
            print("\n")

if __name__ =='__main__':
    main()
