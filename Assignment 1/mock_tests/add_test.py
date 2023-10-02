import unittest

#note the tests are pseudocoded

class TestAdd(unittest.TestCase):
    #check that input add bring correct prompt
    def add_input_test(self):
        #input should be the prompt "add" from the user in command line
        #the result should be the system advancing to the next step of add functionality 
        #output should be a prompt from the SYSTEM to enter eventID
        #test should pass if system advanced to next step
    
    #check that inputing event ID prompts for quantity
    def add_event_test(self):
        #input from user will be an event id
        #result should be checking the event ID against the system
        #system should then move to next step of add functionalty by prompting user for quantity
        #output is system moving to next step and prompting user for quantity
        #test should pass if eventID matches one in the system
    
    #check tickets are added to event
    def add_quantity_test(self):
        #input from user will be quantity to be added and event ID
        #output will be successfully adding tickets to the backend
        #output to user will be SUCCESS notification
        #test will pass if backend is updated

    #check the event log has been updated
    def add_eventlog_test(self):
        #input will be from function to write to the event log 
        #output will be to confirm the transaction has been recorded
        #test will pass if transaction records to event log

    #test for bad event ID
    def add_badeventname_test(self):
        #input will be to provide a badinput (nonmatching event id) to the add function
        #output will be a message that event ID is invalid
        #test should pass if system can not find ID and uses case 
        #to prompt the user for correct info 

    #try bad input for quantity
    def add_badinput_test(self):
        #input will be a nonpositive integer as an amount to add to an event
        #ex -3
        #output will be a failstate in the backend and prompt to user to enter a valid quantity
        #test will Pass if failstate met

    # test adding without admin fails
    #assuming not logged in
    def add_nologin_test(self):
        #input will be an "add" prompt from a non admin account state
        #output wil be a failstate that prompts user about admin status
        #test will pass if proper failstate is reached