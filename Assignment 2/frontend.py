import logging
from backend import Backend

RUN = True
LOGIN_TYPE = None

'''
Configure Logging
'''
logging.basicConfig(filename='daily.log',
                     level=logging.INFO,
                     format= "%(message)s")


class Frontend:
    def __init__(self):
        self.privledge = None
        self.run = True
        self.transaction_count=0
        self.backend = Backend()
    
    def login(self):
        '''
        Login as sales or admin
        '''
        while self.privledge == None:
            userid = input("Enter the session type: ").lower()
            if userid == "sales":
                self.privledge = "sales"
            elif userid == "admin":
                self.privledge = "admin"
            else:
                print("Invalid session type. Please ender admin or sales")
        
        # Import current events file

    def create_event(self):
        event_name = input("Enter event name: ")
        event_date = input("Enter event date (YYYYMMDD): ")
        num_tickets = int(input("Enter number of tickets available: "))
        # Call the backend function to create the event
        result = self.backend.create_event(event_name, event_date, num_tickets)
        if result:
            print("Event created successfully.")
        else:
            print("Failed to create the event.")

    def delete(self):
        if not self.privledge:
            print("You must be logged in as an admin to delete tickets from an event.")
            return

        event_name = input("Enter the name of the event: ")
        ticket_number = int(input("Enter the ticket number to delete: "))

        if not self.backend.event_exists(event_name):
            print("Event not found or cannot delete tickets from it.")
            return

        if not self.backend.ticket_exists(event_name, ticket_number):
            print("Ticket not found or cannot be deleted.")
            return

        confirmation = input(f"Are you sure you want to delete ticket {ticket_number} from the event '{event_name}'? (yes/no): ").lower()

        if confirmation == 'yes':
            result = self.backend.delete_ticket(event_name,ticket_number)

            if result:
                print(f"Ticket: {ticket_number} deleted successfully from event {event_name}")
            else:
                print(f"Failed to delete Ticket: {ticket_number} successfully from event {event_name}")

        else:
            print("Ticket deletion canceled")

    def sell(self):
        event_name = input("Enter the name of the event: ")
        quantity = int(input("Enter the number of tickets to sell: "))

        payment_method = input("Enter payment method: ")
        card_number = input("Enter card number: ")

        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer email: ")

        sale_result = self.backend.sell_tickets(event_name, quantity, payment_method, card_number, customer_name,
                                                customer_email)

        if sale_result["status"] == "success":
            print(f"Sale Successful!")
        else:
            print("Sale failed")

    def logout(self):
        '''
        Logout of current session
        '''
        if not self.privledge:
            print("You are not logged in")
            return
        self.privledge = None
        
        
    def add(self):
        '''
        Add a new event
        '''
        valid_input = False
        # Test for valid input
        while not valid_input:
            event_name = input("enter event name: ")
            '''
            if condition not true:
                print("Invalid event name")
                continue
            '''
            event_date = input('enter event date YYYYMMDD: ')
            num_tickets = input('enter number of tickets: ')
            valid_input = True
        
        '''
        result = self.backend.add_event(event_name, event_date, num_tickets)
        if result == False:
            print("Event already exists")
            return
        '''
        
        print("Event added successfully")
        
        # Increment transaction count
        self.transaction_count += 1
        transaction_code = str(self.transaction_count).zfill(2)
        
        # Save transaction to log
        event_transaction = "{}_{}_{}_{}".format(transaction_code,event_name,event_date,num_tickets)
        return event_transaction
        
        
    def main(self):
        while self.run:
            command = input("please enter command: ").lower()
            
            # If not logged in, only allow login command
            if not self.privledge:
                if command == "login":
                    self.login()
                else:
                    print("You are not logged in, please 'login' to continue")
                continue
                
            # If logged in, allow all commands    
            match command:
                case "login":
                    if self.privledge:
                        print("You are already logged in")
                case "logout":
                    self.logout()
                case "add":
                    self.add()
                case "create":
                    self.create_event()
                case "delete":
                    self.delete()
                case "sell":
                    self.sell()

                    '''
                case "delete":
                    delete()
                case "create":
                    create()
                case "sell"
                    sell()
                '''
                case ("exit" | "quit" | "q" | 'x'):
                    self.run = False
                case _ :
                    print("not a valid command")