import unittest

#note tests are psuedocoded
#assume login as admin unless specified 
class TestDelete(unittest.TestCase):

    #tests that inputing delete will bring up prompt
    def delete_input_test(self):
        #input should be the prompt "delete" from the user in command line
        #the result should be the system advancing to the next step of delete functionality 
        #output should be a prompt from the SYSTEM to enter event ID
        #test should pass if system advanced to next step of delete process

    #test deleting a quantity for a valid event
    def delete_tickets_test(self):
        #input from user will be an event id and quantity
        #result should be checking the event ID against the system
        #system should then delete the quantity of tickets from event
        #output is system moving to next step and prompting user for quantity
        #test should pass if eventID matches one in the system

    #test deleting the actual event
    def delete_event_test(self):
        #input from user will be keyword like "ALL" for delete processs
        #system should then delete the entire event
        #output is system deleting event and confirming with USER
        #test should pass if eventID matches one in the system

    #test the deletion quantity is being correctly captured in eventslog
    def delete_ticket_transaction_test(self):
        #input will be from a function to delete a given quantity and write to the event log 
        #output will be to confirm the transaction has been recorded
        #test will pass if transaction records to event log

    #test deleting entire event is captured in events log
    def delete_event_transaction_test(self):
        #input will be from a function to delete an event and record to the event log
        #output will be to confirm the transaction has been recorded
        #test will pass if transaction records to event log 

    #test delete without admin priveledges
    def delete_noadmin_test(self):
        #input will be an "delete" prompt from a non admin account state
        #output wil be a failstate that prompts user about admin status
        #test will pass if poper failstate is reached

    #test bad event ID will fail
    def delete_wrongevent_test(self):
        #input will be an invalid eventID to delete
        #ex 999999999
        #output will be a failstate in the backend and prompt to user to enter a valid quantity
        #test will Pass if failstate met
    
    #test bad quantity input will fail
    def delete_wrongticket_test(self):
        #input will be a nonpositive integer as an amount to delete from an event
        #ex -3
        #output will be a failstate in the backend and prompt to user to enter a valid quantity
        #test will Pass if failstate met
    
    #test you cant delete more than number of available tickets
    def delete_toomany(self):
        #input will be a quantity greater than the max number of tickets available to the delete function
        #output will be a failstate and prompt to user that quantity is greater than max
        #test will pass if failstate is reached
