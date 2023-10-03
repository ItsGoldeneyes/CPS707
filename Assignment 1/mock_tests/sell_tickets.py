import unittest

# Ticket Selling Service code and functions here.

def sell_tickets(user, event, quantity, payment_method, card_number, customer_name, customer_email):
    # Assuming ticket selling logic goes here
    # For this Assignment, we'll assume a simplified result dictionary
    result = {
        "status": "success",
        "total_price": quantity * 50,  # Assuming a ticket price of $50
        "confirmation_code": "ABC123XYZ"
    }
    return result

class TestSellTickets(unittest.TestCase):
    def test_sell_tickets_success(self):
        user = "sales_user"
        event = "Event_Name_1"
        quantity = 2
        payment_method = "Credit Card"
        card_number = "1234-5678-9876-5432"
        customer_name = "Rick Ross"
        customer_email = "RR@example.com"

        result = sell_tickets(user, event, quantity, payment_method, card_number, customer_name, customer_email)

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["total_price"], 100)
        self.assertEqual(result["confirmation_code"], "ABC123XYZ")

    def test_sell_tickets_invalid_event(self):
        user = "sales_user"
        event = "Non_Existent_Event"
        quantity = 2
        payment_method = "Credit Card"
        card_number = "1234-5678-9876-5432"
        customer_name = "Okonjo Iweala"
        customer_email = "Iweala@example.com"

        result = sell_tickets(user, event, quantity, payment_method, card_number, customer_name, customer_email)

        self.assertEqual(result["status"], "error")
        self.assertEqual(result["message"], "Event not available for sale")

    def test_sell_tickets_insufficient_quantity(self):
        user = "sales_user"
        event = "Event_Name_2"
        quantity = 10  # Assuming only 5 tickets available
        payment_method = "Credit Card"
        card_number = "1111-2222-3333-4444"
        customer_name = "Tony Elumelu"
        customer_email = "TOE@example.com"

        result = sell_tickets(user, event, quantity, payment_method, card_number, customer_name, customer_email)

        self.assertEqual(result["status"], "error")
        self.assertEqual(result["message"], "Insufficient ticket quantity available")

    def test_sell_tickets_payment_failure(self):
        user = "sales_user"
        event = "Event_Name_3"
        quantity = 3
        payment_method = "Invalid Payment Method"
        card_number = "1234-5678-9876-5432"
        customer_name = "Bob Manuel"
        customer_email = "bob@example.com"

        result = sell_tickets(user, event, quantity, payment_method, card_number, customer_name, customer_email)

        self.assertEqual(result["status"], "error")
        self.assertEqual(result["message"], "Payment transaction failed")

    def test_sell_tickets_customer_information(self):
        user = "sales_user"
        event = "Event_Name_4"
        quantity = 1
        payment_method = "Credit Card"
        card_number = "5555-6666-7777-8888"
        customer_name = "John cena"
        customer_email = "CantSeeMe@example.com"

        result = sell_tickets(user, event, quantity, payment_method, card_number, customer_name, customer_email)

        # Assuming the result contains customer information
        self.assertEqual(result["customer_name"], "John cena")
        self.assertEqual(result["customer_email"], "CantSeeMe@example.com")

    def test_sell_tickets_inventory_update(self):
        user = "sales_user"
        event = "Event_Name_5"
        quantity = 2
        payment_method = "Credit Card"
        card_number = "9999-0000-1111-2222"
        customer_name = "Shawn Michaels"
        customer_email = "HBK@example.com"

        result = sell_tickets(user, event, quantity, payment_method, card_number, customer_name, customer_email)

        # Assuming the result contains updated ticket inventory information
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["available_tickets"], 3)  # Assuming there were initially 5 tickets available


if __name__ == '__main__':
    unittest.main()
