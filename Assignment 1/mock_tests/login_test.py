import unittest
from functions import login


class TestLogin(unittest.TestCase):
    
    def login_sales(self):
        '''
        Test that a sales user can login
        '''
        # Expected input
        input_username = "sales_username123"
        input_password = "sales_password123"
        # Expected output: True
        result = login(input_username, input_password)
       
        self.assertEqual(result, True)
        
        
    def login_admin(self):
        '''
        Test that an admin user can login
        '''
        # Expected input
        input_username = "admin_username123"
        input_password = "admin_password123"
        # Expected output: True
        result = login(input_username, input_password)
        
        self.assertEqual(result, True)
        
        
    def login_restricted(self):
        '''
        Test that no other commands are accepted before login
        '''
        # Expected input
        input = "add tickets 52"
        # Expected output: False
        result = login(input)
        
        self.assertEqual(result, False)
        
        
    def login_bad(self):
        '''
        Test that a bad username or password fails
        '''
        # Expected input
        input_username = "bad_username"
        input_password = "bad_password"
        # Expected output: False
        result = login(input_username, input_password)
        
        self.assertEqual(result, False)
        
    
    def login_consecutive(self):
        '''
        Test that a user can't login after logging in
        '''
        # Setup
        login("admin_username123", "admin_password123")
        
        # Expected input
        input_username = "sales_username123"
        input_password = "sales_password123"
        # Expected output: False
        result = login(input_username, input_password)
        
        self.assertEqual(result, False)
        
        
    
        