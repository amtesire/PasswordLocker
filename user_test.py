import unittest
from user import User
from user import Account
class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Gisele", "Tesire", "tesigi", "peaceful")
    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Gisele")
        self.assertEqual(self.new_user.last_name, "Tesire")
        self.assertEqual(self.new_user.user_name, "tesigi")
        self.assertEqual(self.new_user.password, "peaceful")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user listed
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Gisele", "Tesire", "tegizo", "dolphins")
        test_user.save_user()
        self.assertEqual(len(User.user_list),3)
    def test_delete_user(self):
        '''
        test_delete_user to test if we van remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Gisele", "Tesire", "gizote", "peaceful1")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),2)
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by their username and display infformation
        '''
        self.new_user.save_user()
        test_user = User("Gisele", "Tesire", "tesigi", "mullah")
        test_user.save_user()
        found_user = User.find_by_username("tesigi")
        self.assertEqual(found_user.user_name,"mullah")
    def test_find_user_by_password(self):
        '''
        test to check if we can find a user by their password
        '''
        self.new_user.save_user()
        test_user = User("Gisele", "Tesire", "tesiregisele", "lovely")
        test_user.save_user()
        found_password = User.find_by_userpassword("lovely")
        self.assertEqual(found_password.password,"lovely")
    def test_display_user_information(self):
        '''
        test to check if we can be able to display users saved in user_list
        '''
        self.assertEqual(User.display_userInfo(),User.user_list)
class TestAccount(unittest.TestCase):
    def setUp(self):
        self.new_account = Account("Instagram", "Gisele", "sweet")
    def test_init(self):
        self.assertEqual(self.new_account.account_name,"Instagram")
        self.assertEqual(self.new_account.account_userName,"Gisele")
        self.assertEqual(self.new_account.account_password,"sweet")
    def test_save_account(self):
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list),2)
    def tearDown(self):
        Account.account_list = []
    def test_display_account_credentials(self):
        self.assertEqual(Account.display_accounts(),Account.account_list)
    def test_delete_account(self):
        self.new_account.save_account()
        test_account = Account("Twitter", "Gisele", "sweeter")
        test_account.save_account()
        test_account.delete_account()
        self.assertEqual(len(Account.account_list),1)
    def test_find_account_by_name(self):
        self.new_account.save_account()
        test_account = Account("Medium", "Tesire", "sweetest")
        test_account.save_account()
        found_account = Account.find_by_accountName("Medium")
        self.assertEqual(found_account.account_name,"Medium")
if __name__ == '__main__':
    unittest.main()
