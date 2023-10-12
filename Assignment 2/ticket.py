from functions import login, logout, add
import logging

logging.basicConfig(filename='daily.log',
                     level=logging.INFO,
                     format= "%(message)s")

while True:
    command = input("please enter command: ").lower()

    match command:
        case "login":
            login()
        case "logout":
            logout()
        case ("exit" | "quit" | "q" | 'x'):
            quit()
        case "add":
            transaction = add()
            print("Added transaction: ", transaction)
            logging.info(transaction)
            '''
        case "delete":
            delete()
        case "create":
            create()
        case "sell"
            sell()
        case "return"
            return            
        '''
        case _ :
            print("not a valid command")

