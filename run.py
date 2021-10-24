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
