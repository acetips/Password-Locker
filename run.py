#!/usr/bin/env python3.8

from locker import User
from locker import Credentials

import random
import string
ncmx,

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

def generate_random_password(length = 4):
    '''
    A function that generates a random password for the user
    '''
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def save_credentials(credential):
    '''
    A function to save new credentials of the user
    '''
    credential.save_credentials()

def create_credential(website,website_username,website_password):
    '''
    A function for creating or adding new credentials
    '''
    new_credentials = Credentials(website,website_username,website_password)
    return new_credentials

def delete_credentials(credential):
    '''
    a function for deleting the saved credentials of the user
    '''
    credential.delete_credentials()

def find_credentials(website):
    '''
    A function to enable the user to find his or her credential
    '''
    return Credentials.find_by_website(website)

def show_all_credentials():
    '''
    A function to display all the user's credentials
    '''
    return Credentials.credentials_list

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
            print("To generate a random password, enter 'gg';To create your preferred password, enter 'pp':")
            user_input = input().lower()
            if user_input == 'gg':
                print("Preferred username:")
                username = input()
                mypassword = generate_random_password()
                print(f"Your password is {mypassword}")
            else:
                print("Preferred username:")
                username = input()
                print("Preferred password:")
                mypassword = input()
                print()

            save_user(create_passwordlocker_account(first_name,last_name,username,mypassword))
            print('\n')
            print("Congratulations!Your account has been created successfully. Here are your details:")
            print(f"First name:{first_name} Last name:{last_name} Username:{username} Password:{mypassword}")
            print('\n')
            print("To login, enter your username:")
            created_username = input()
            print("Enter your password:")
            created_password = input()

            if created_username != username or created_password != mypassword:
                print("Invalid username and/or password")
                print('\n')
                print("Enter username")
                created_username = input()
                print("Enter password")
                created_password = input()
            else:
                print("Login successful!")
                print('\n')
                print("Would you like to:")
                print("cc - Add or create a new credential")
                print("dd - Delete a credential")
                print("dis - Display your credentials")
                print("ff - Find a credential")
                user_input = input().lower()
                if user_input == 'cc':
                    print("Create a new credential")
                    print("* "*6)
                    print("Enter website or app name Eg Github:")
                    website = input()
                    print("To generate a random password, enter 'gg';To create your preferred password, enter 'pp':")
                    user_input = input().lower()
                    if user_input == 'gg':
                        print("Preferred username:")
                        website_username = input()
                        website_password = generate_random_password()
                        print(f"Your password is {website_password}")
                        save_credentials(create_credential(website,website_username,website_password))
                        print('\n')
                        print(f"Congratulations!Your {website} account details have been saved successfully.")
                        print('* '*6)
                        print("Enter 'dis' to display your credentials")
                        user_input = input().lower()
                        if user_input == 'dis':
                            print('Here are your credentials:')
                            print(f'{website}|{website_username}|{website_password}')
                        else:
                            break
                            
                    else:
                        print("Preferred username:")
                        website_username = input()
                        print("Preferred password:")
                        website_password = input()
                        print()
                        print("Confirm your password for the specified website above:")
                        website_password = input()
                        print()

                        save_credentials(create_credential(website,website_username,website_password))
                        print('\n')
                        print(f"Congratulations!Your {website} account details have been saved successfully.")
                        print('* '*6)
                        print("Enter 'dis' to display your credentials")
                        user_input = input().lower()
                        if user_input == 'dis':
                            print('Here are your credentials:')
                            print(f'{website}|{website_username}|{website_password}')
                        else:
                            break
                
                elif user_input == 'dd':
                    print("Enter the website or app name whose credentials you would like to delete:")
                    print("* "*6)
                    dispensable_credential_website = input()
                    dispensable_credential = find_credentials(dispensable_credential_website)
                    print('\n')
                    print(f"Your {dispensable_credential_website} credentials have been successfully deleted!")
                    break
                
                elif user_input == 'dis':
                    if show_all_credentials():
                        print("Here are all your credentials:")
                        for credentials in show_all_credentials():
                            print(f'{credentials.website} {credentials.website_username} {credentials.website_password}')
                            # print(f'{credentials_list}')

                    else:
                        print("You have no saved credentials at the moment.")
                        break

                

        elif user_input == 'la':
            print ("Login to your account")
            print("*"*6)
            print("Enter your username:")
            username = input()
            print("Enter your password")
            mypassword = input()
            if username != username or mypassword != mypassword:
                print("Invalid username and/or password")
                print("Enter username:")
                username = input()
        
                print("Enter password:")
                password = input()
            else:
                print("Login successful!")
                print('\n')
                print("Would you like to:")
                print("cc - Add or create a new credential")
                print("dd - Delete a credential")
                print("dis - View your credentials")
                print("ff - Find a credential")
                user_input = input().lower()
                if user_input == 'cc':
                    print("Create a new credential")
                    print("* "*6)
                    print("Enter website or app name Eg Github:")
                    website = input()
                    print("To generate a random password, enter 'gg';To create your preferred password, enter 'pp':")
                    user_input = input().lower()
                    if user_input == 'gg':
                        print("Preferred username:")
                        website_username = input()
                        website_password = generate_random_password()
                        print(f"Your password is {website_password}")
                    else:
                        print("Preferred username:")
                        website_username = input()
                        print("Preferred password:")
                        website_password = input()
                        print()
                    print("Confirm your password for the specified website above:")
                    website_password = input()
                    print()

                    save_credentials(create_credential(website,website_username,website_password))
                    print('\n')
                    print(f"Congratulations!Your {website} account details have been saved successfully.")
                    print('* '*6)
                    print("Enter 'dis' to display your credentials")
                    user_input = input().lower()
                    if user_input == 'dis':
                        print('Here are your credentials:')
                        print(f'{website}|{website_username}|{website_password}')
                    else:
                        break
                
                elif user_input == 'dd':
                    print("Enter the website or app name whose credentials you would like to delete:")
                    print("* "*6)
                    dispensable_credential_website = input()
                    dispensable_credential = find_credentials(dispensable_credential_website)
                    print('\n')
                    print(f"Your {dispensable_credential_website} credentials have been successfully deleted!")
                    break
                
                elif user_input == 'vv':
                    if show_all_credentials():
                        print("Here are all your credentials:")
                        for credentials in show_all_credentials():
                            print(f'{credentials.website} {credentials.website_username} {credentials.website_password}')
                            # print(f'{credentials_list}')

                    else:
                        print("You have no saved credentials at the moment.")
                        break


        # elif user_input == 'la':
        #     print("Account login")
        #     print("*"*6)
        #     print("Username:")
        #     username = input()
        #     print("Enter your password:")
        #     mypassword = input()
        #     print('\n')
        
        elif user_input == 'ex':
            print("We are sad to see you go:(.")
            break
        
        else:
            print("Invalid user entry. kindly re-enter a valid command")
            print("\n")

if __name__ =='__main__':
    main()
