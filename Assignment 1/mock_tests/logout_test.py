import unittest
from functions import login, logout, transaction_file_check


class TestLogout(unittest.TestCase):
    
    def setUp(self):
        username = "sales_username123"
        password = "sales_password123"
        login(username, password)
    
    def logout_success(self):
        '''
        Test that a user can logout
        '''
        # Expected input
        input = "logout"
        # Expected output: True
        result = logout(input)
        
        self.assertEqual(result, True)
        
        
    def logout_transaction_file(self):
        '''
        Tests if transaction file is created after a successful logout
        '''
        # Setup
        logout("logout")
        
        # Expected output: True
        result = transaction_file_check()
        
        
        self.assertEqual(result, True)
        
        
    def logout_nologin(self):
        '''
        Test that a user can't logout without logging in
        '''
        # Setup
        logout("logout")
        
        # Expected input
        input = "logout"
        # Expected output: False
        result = logout(input)
        
        self.assertEqual(result, False)