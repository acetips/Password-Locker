class User:
    '''
    To initialize the User instances
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

class Credentials:

    

    