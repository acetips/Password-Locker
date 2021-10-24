import unittest
from locker import User, Credentials

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

    def tearDown(self):
        '''
        method that clears the locker_list after running each test
        '''
        User.locker_list=[]

    def test_save_user(self):
        '''
        a test to check if the user object is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.locker_list),1)

    def

class TestCredentials(unittest.TestCase):
    '''
    Test class to define test cases for behaviours in the credentials class
    '''
    def setUp(self):
        '''
        method to run before the test cases
        '''
        self.new_credentials = Credentials("Twitter", "PerezTweets", 0000)

    def test_init(self):
        '''
        method to test if object is initialized properly
        '''

        self.assertEqual(self.new_credentials.website, "Twitter")
        self.assertEqual(self.new_credentials.website_username, "PerezTweets")
        self.assertEqual(self.new_credentials.website_password,0000)

    def tearDown(self):
        '''
        method to clear each test case after running the tests
        '''
        Credentials.credentials_list = []
    
    def save_credentials(self):
        '''
        method to test if user credentials are saved
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


    def test_multiple_credentials(self):
        '''
        a test to save user credentials for multiple websites or applications
        '''
        self.new_credentials.save_credentials()
        another_credential = Credentials("Instagram","PerezGrams", 1111)
        another_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_deleting_credentials(self):
        '''
        a test for deleting a user's credentials
        '''
        self.new_credentials.save_credentials()
        another_credential = Credentials("Instagram","PerezGrams", 1111)
        another_credential.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_by_website(self):
        self.new_credentials.save_credentials()
        another_credential = Credentials("Instagram","PerezGrams", 1111)
        another_credential.save_credentials()

        found_credentials = Credentials.find_by_website("Instagram")
        self.assertEqual(found_credentials.website_username, another_credential.website_username)

        
if __name__ == '__main__':
    unittest.main()