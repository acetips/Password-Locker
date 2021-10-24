class User:
    '''
    class for initializing the User instances
    '''
    locker_list = [] #empty locker list

    def __init__(self,first_name,last_name,username):
        '''
        __init__ method that defines the objects' properties
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
    
    def save_user(self):
        '''
        method to save user objects into the locker_list
        '''
        User.locker_list.append(self)

    @classmethod
    def user_exists(cls, username):
        for user in cls.locker_list:
            if user.username == username:
                return True
        return False

class Credentials:
    '''
    class for initializing the user's credentials
    '''
    credentials_list =[]#empty list for user details

    def __init__(self,website,website_username,website_password):
        '''
        method to define object's properties
        '''
        self.website = website
        self.website_username = website_username
        self.website_password = website_password

    def save_credentials(self):
        '''
        method to save new credentials of the user
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        a method for deleting the saved credentials of the user
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_website(cls, website):
        for credential in cls.credentials_list:
            if credential.website == website:
                return credential
    
    def test_display_credentials(cls):
        return cls.credentials_list

   

    # @classmethod
    # def verify_credentials(cls, name, lock):
    #     '''
    #     Method that checks if the username and password are correct
    #     '''
    #     for user in cls.credentials_list:
    #         if user.user_name == name and user.password == lock:
    #             return user
    #     return 0
    