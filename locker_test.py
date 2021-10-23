import unittest
from locker import User

class TestUser(unittest.TestCase):
    '''
    class to define test cases for user class behavior
    '''
    def setUp(self):
        '''
        Set up method to run before each test
        '''
        self.new_user= User("Emelda", "Perez", "acetips")

    def test_init(self):
        '''
        test_init method to test if object is properly initialized
        '''
        self.assertEqual(self.new_user.first_name,"Emelda")
        self.assertEqual(self.new_user.last_name,"Perez")
        self.assertEqual(self.new_user.username,"acetips")

    def test_save_user(self):
        '''
        a test to ckeck if the user object is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.locker_list),1)


if __name__ == '__main__':
    unittest.main()