import unittest
import ticket
import eventslog

class TestAdd(unittest.TestCase):
    #check that input add bring correct prompt
    def add_input_test(self):
        result = ticket.add()
        self.assertEqual(result, "Enter Event Number")
    
    #check that inputing event ID prompts for quantity
    def add_event_test(self):
        result = ticket.addEvent(eventID)
        self.assertEqual(result, "Enter Ticket Quantity")
    
    #check tickets are added to event
    def add_quantity_test(self):
        result = ticket.addEvent(eventID).addQuantity(quantity)
        self.assertEqual(result, (quantity, "tickets added to event ", eventID))

    #check the event log has been updated
    def add_eventlog_test(self):
        result = ticket.addEvent(eventID).addQuantity(quantity).assertLogs()
        self.assertIsInstance(result, eventslog)

    #test for bad event ID
    def add_badeventname_test(self):
        eventID = "BADINPUT"
        result = ticket.addEvent(eventID)
        self.assertEqual(result, "Invalid Event ID")

    #try bad input for quantity
    def add_badinput_test(self):
        quantity = -3
        result = ticket.addEvent(eventID).addQuantity(quantity)
        self.assertEqual(result, "Invalid Quantity entered")

    # test adding without admin fails
    #assuming not logged in
    def add_nologin_test(self):
        result = ticket.add()
        self.assertEqual(result, "Must be Admin to Add")