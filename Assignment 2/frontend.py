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