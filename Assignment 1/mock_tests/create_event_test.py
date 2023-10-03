import unittest
from functions import login, logout, create_event, set_date, transaction_file_check


class TestCreateEvent(unittest.TestCase):
    
    def setUp(self):
        
        username = "admin_username123"
        password = "admin_password123"
        login(username, password)
        
        event_name = "Event1"
        date = "20231129"
        ticket_count = 100
        
        create_event(event_name, date, ticket_count)
        
    def create_event_success(self):
        '''
        Test that an event can be created
        '''
        # Expected input
        input_event_name = "Event2"
        input_date = "20231203"
        input_ticket_count = 100
        # Expected output: True
        result = create_event(input_event_name, input_date, input_ticket_count)
        
        self.assertEqual(result, True)
        
    
    def create_event_noadmin(self):
        '''
        Test that an event cannot be created if not logged in as admin
        '''
        # Setup
        logout("logout")
        username = "sales_username123"
        password = "sales_password123"
        login(username, password)
        
        # Expected input
        input_event_name = "Event2"
        input_date = "20231203"
        input_ticket_count = 100
        # Expected output: False
        result = create_event(input_event_name, input_date, input_ticket_count)
        
        self.assertEqual(result, False)
        
        
    def create_event_datefail(self):
        '''
        Test that an event's date field is in the correct format by checking if it's between tomorrow and 2 years from today
        '''
        # Setup
        set_date("20231002")
        
        # Expected input
        input_event_name = "Event2"
        input_date = "20231001"
        input_ticket_count = 100
        # Expected output: False
        result = create_event(input_event_name, input_date, input_ticket_count)
        
        self.assertEqual(result, False)
        
    
    def create_event_amountfail(self):
        '''
        Test that an event's ticket count is 0<x<10000
        '''
        
        # Expected input
        input_event_name = "Event2"
        input_date = "20231203"
        input_ticket_count = 100000
        # Expected output: False
        result = create_event(input_event_name, input_date, input_ticket_count)
        
        self.assertEqual(result, False)
        
    
    def create_event_namefaillength(self):
        '''
        Tests if name is fewer than or equal to 15 characters
        '''
        
        # Expected input
        input_event_name = "This is a really long event name"
        input_date = "20231203"
        input_ticket_count = 100
        # Expected output: False
        result = create_event(input_event_name, input_date, input_ticket_count)
        
        self.assertEqual(result, False)
        
        
    def create_event_namefailcopy(self):
        '''
        Tests if name is unique
        '''
        
        # Expected input
        input_event_name = "Event1"
        input_date = "20231203"
        input_ticket_count = 100
        # Expected output: False
        result = create_event(input_event_name, input_date, input_ticket_count)
        
        self.assertEqual(result, False)
        
        
    def create_event_eventtransactioncheck(self):
        '''
        Tests if event is recorded in event transactionfile
        '''
        
        result = transaction_file_check("Event1")
        
        self.assertEqual(result, True)