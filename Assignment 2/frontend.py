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
        self.privilege = None
        self.run = True
        self.transaction_count=0
        self.backend = Backend()
    
    def login(self):
        '''
        Login as sales or admin
        '''
        while self.privilege == None:
            userid = input("Enter the session type: ").lower()
            if userid == "sales":
                self.privilege = "sales"
            elif userid == "admin":
                self.privilege = "admin"
            else:
                print("Invalid session type. Please ender admin or sales")
        
        # Import current events file
        
        
    def logout(self):
        '''
        Logout of current session
        '''
        if not self.privilege:
            print("You are not logged in")
            return
        self.privilege = None
        
        
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
            if not self.privilege:
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
                    '''
                case "delete":
                    delete()
                case "create":
                    create()
                case "sell"
                    sell()
                '''
                #Exit case to exit the program
                case ("exit" | "quit" | "q" | 'x'):
                    self.run = False

                #help case to display options to user
                case ("help" | 'h'):
                    #options for admin user
                    if (self.privilege == "admin"):
                        print(
                            "Enter: 'create' for new event | 'add' to add tickets | " +
                               "'delete' to remove events or tickets |" +
                               "'sell' if tickets have been sold to customer | 'return' to refund sold tickets |" +
                                "'logout' to logout |'exit' to exit"
                            )
                    #options for sales user 
                    elif (self.privilege == "sales"):
                        print(
                            "Enter: " +
                               "'sell' if tickets have been sold to customer | 'return' to refund sold tickets |" +
                                "'logout' to logout |'exit' to exit"
                            )
                        
                #handles an invalid command line input
                case _ :
                    print("not a valid command")