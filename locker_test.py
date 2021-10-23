import unittest
from users import User

class TestUser(unittest.TestCase):
    '''
    class to define test cases for user class behavior
    '''
    def setUp(self):
        '''
        Set up method to run before each test
        '''
        self.new_user= User("Emelda", "Perez", "acetips")