import unittest
import ticket
import eventslog

#assume login as admin unless specified 
class TestDelete(unittest.TestCase):

    #tests that inputing delete will bring up prompt
    def delete_input_test(self):
        input = ticket.delete()
        self.assertEqual(input, "Enter Event Number")

    #test deleting a quantity for a valid event
    def delete_tickets_test(self):
        input = ticket.deleteEvent(eventID)
        self.assertEqual(input, "Enter Ticket Quantity")

    #test deleting the actual event
    def delete_event_test(self):
        input = ticket.deleteEvent(eventID).deleteQuantity("ALL")
        output = (eventID, " Deleted")
        self.assertEqual(input, output)

    #test the deletion quantity is being correctly captured in eventslog
    def delete_ticket_transaction_test(self):
        input = ticket.deleteEvent(eventID).deleteQuantity(quantity).assertLogs()
        self.assertIn(input, eventslog)

    #test deleting entire event is captured in events log
    def delete_event_transaction_test(self):
        input = ticket.deleteEvent(eventID).deleteQuantity("ALL").assertLogs()
        self.assertIn(input, eventslog)   

    #test delete without admin priveledges
    def delete_noadmin_test(self):
        input = ticket.delete()
        self.assertEqual(input, "Must be Admin to Delete")

    #test bad event ID will fail
    def delete_wrongevent_test(self):
        eventID = "BADINPUT"
        input = ticket.deleteEvent(eventID)
        self.assertEqual(input, "Invalid event ID")
    
    #test bad quantity input will fail
    def delete_wrongticket_test(self):
        quantity = -3
        input = ticket.deleteEvent(eventID).deleteQuantity(quantity)
        self.assertEqual(input, "Invalid Quantity Entered")
    
    #test you cant delete more than number of available tickets
    def delete_toomany(self):
        max_number = ticket.event(eventID).quantity()
        quantity = max_number + 1
        input =  ticket.deleteEvent(eventID).deleteQuantity(quantity)
        self.assertEqual(input, "Quantity is more than Max")
