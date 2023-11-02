import logging
from backend import Backend
from datetime import datetime

class Frontend:
    def __init__(self):
        self.privilege = None
        self.run = True
        self.transactions = []
        self.current_events = []
        self.backend = Backend()
        
        # Configure logging
        logging.basicConfig(filename='daily.log',
                     level=logging.INFO,
                     format= "%(message)s")
        
    
    def login(self):
        '''
        Login as sales or admin
        '''
        userid = input("Enter the session type: ").lower()
        if userid == "sales":
            self.privilege = "sales"
        elif userid == "admin":
            self.privilege = "admin"
        else:
            print("Invalid session type. Please enter admin or sales")
            return
                
        # Create current events file if doesn't exist
        with open("current_events.txt", "a") as f:
            pass
        
        # Verify current events file and import it
        with open("current_events.txt", "r") as f:
            current_events = f.readlines()
            if current_events:
                self.current_events = current_events
                # self.backend.import_events(current_events)
    
    
    def logout(self):
        '''
        Logout of current session
        '''
        if not self.privilege:
            print("You are not logged in")
            return
        
        # Append end code to current events
        self.transactions.append("00")
        
        # Create transaction file from current events
        with open(f"transaction_files/transaction_file{datetime.now().strftime('%Y%m%d')}.txt", "w") as f:
            for event in self.transactions:
                f.write(event+"\n")
        
        # Set current events to empty
        self.transactions = []
        
        # Set login privledge to none
        self.privilege = None
        print("You have been logged out.")
        
    
    def check_transaction_file(self):
        with open(f"transaction_files/transaction_file{datetime.now().strftime('%Y%m%d')}.txt", "r") as f:
            transaction_file = f.readlines()
            if not transaction_file:
                return False
            
            for line in transaction_file:
                print(line, end="")
             
        
    def create(self):
        '''
        Create a new event
        '''
        if self.privilege != "admin":
            print("You are not authorized to create events.")
            return
        
        # Test for valid input
        event_name = input("Enter event name: ")
        event_date = input("Enter event date (YYYYMMDD): ")
        num_tickets = int(input("Enter number of tickets: "))
        
        # Input validation
        if len(event_name) > 15:
            print("Event name must be less than or equal to 15 characters.")
            return
        if len(event_date) != 8 or not event_date.isdigit():
            print("Event date must be in the format YYYYMMDD.")
            print(len(event_date), event_date)
            return
        if int(event_date) <= int(datetime.now().strftime('%Y%m%d')) or int(event_date) > int(datetime.now().strftime('%Y%m%d')) + 20000:
            print("Event date must be between tomorrow and 2 years from today.")
            return
        if num_tickets <= 0 or num_tickets >= 10000:
            print("Number of tickets must be greater than 0 and less than 10000.")
            return
        # Check transaction file for event
        for event in self.transactions:
            if "03 " + event_name.replace(' ', '_').ljust(15, "_") in event:
                print("Event already exists.")
                return
        # Check current events for event
        for event in self.current_events:
            if event_name.replace(' ', '_').ljust(15, "_") in event:
                print("Event already exists.")
                return
            
        # Call the backend function to create the event
        # result = self.backend.create_event(event_name, event_date, num_tickets)
        result = True
        if result:
            self.transactions.append(f"03 {event_name.replace(' ', '_').ljust(15, "_")} {event_date} {str(num_tickets).rjust(4, '0')}")
            print("Event created successfully.")
        else:
            print("Failed to create the event.")


    def delete(self):
        '''
        Delete ticket from event
        '''
        valid_input = False
        # Test for valid input
        event_name = input("Enter the name of the event: ")
        ticket_number = int(input("Enter the ticket number to delete: "))
        valid_input = True

        # if not self.backend.event_exists(event_name):
        #     print("Event not found or cannot delete tickets from it.")
        #     return

        # if not self.backend.ticket_exists(event_name, ticket_number):
        #     print("Ticket not found or cannot be deleted.")
        #     return

        confirmation = input(f"Are you sure you want to delete ticket {ticket_number} from the event '{event_name}'? (yes/no): ").lower()

        if confirmation == 'yes':
            # result = self.backend.delete_ticket(event_name,ticket_number)
            result = True

            if result:
                print(f"Ticket: {ticket_number} deleted successfully from event {event_name}")
            else:
                print(f"Failed to delete Ticket: {ticket_number} successfully from event {event_name}")
        else:
            print("Ticket deletion canceled")


    def sell(self):
        '''
        Sell tickets to customer
        '''
        valid_input = False
        # Test for valid input
        event_name = input("Enter the name of the event: ")
        quantity = int(input("Enter the number of tickets to sell: "))

        payment_method = input("Enter payment method: ")
        card_number = input("Enter card number: ")

        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer email: ")
        valid_input = True

        # sale_result = self.backend.sell_tickets(event_name, quantity, payment_method, card_number, customer_name,
                                                # customer_email)
        sale_result = {"status": "success"}

        if sale_result["status"] == "success":
            print(f"Sale Successful!")
        else:
            print("Sale failed")
        
        
    def add(self):
        '''
        Add a new event
        '''
        valid_input = False
        # Test for valid input
        event_name = input("enter event name: ")
        '''
        if condition not true:
            print("Invalid event name")
            continue
        '''
        event_date = input('enter event date YYYYMMDD: ')
        num_tickets = input('enter number of tickets: ')
        valid_input = True
        
        # result = self.backend.add_event(event_name, event_date, num_tickets)
        # if result == False:
        #     print("Event already exists")
        #     return
        
        print("Event added successfully")
        
        # Increment transaction count
        self.transaction_count += 1
        transaction_code = str(self.transaction_count).zfill(2)
        
        # Save transaction to log
        event_transaction = "{}_{}_{}_{}".format(transaction_code,event_name,event_date,num_tickets)
        return event_transaction
    
    def help(self):
        '''
        Displays a help menu
        '''
        # Options for an admin user
        if (self.privilege == "admin"):
            print("\t" +
                    "'create' for new event \n\t" + 
                    "'add' to add tickets \n\t" +
                    "'delete' to remove events or tickets \n\t" +
                    "'sell' if tickets have been sold to customer \n\t"  + 
                    "'return' to refund sold tickets \n\t" +
                    "'logout' to logout \n\t" +
                    "'exit' to exit"
                )
        # Options for a sales user 
        elif (self.privilege == "sales"):
            print( "\t"+
                    "'sell' if tickets have been sold to customer \n\t" + 
                    "'return' to refund sold tickets \n\t" +
                    "'logout' to logout |'exit' to exit"
                )   
        
    def main(self):
        while self.run:
            command = input("Please enter command: ").lower()
            
            
            # Force non-logged in users to login or quit
            if command in ["exit", "quit", "q", 'x']:
                print("Exiting program...")
                self.run = False
                continue
            elif not self.privilege:
                if command == "login":
                    self.login()
                else:
                    print("You are not logged in, please 'login' to continue")
                continue
                
            # If logged in, allow all commands    
            match command:
                case "login":
                    if self.privilege:
                        print("You are already logged in")
                case "logout":
                    self.logout()
                case "add":
                    self.add()
                case "create":
                    self.create()
                case "delete":
                    self.delete()
                case "sell":
                    self.sell()
                case ("help" | 'h'):
                    self.help()
                case "transaction":
                    self.check_transaction_file()
                case ("exit" | "quit" | "q" | 'x'):
                    print("Exiting program...")
                    self.run = False
                case _ :
                    print("not a valid command")