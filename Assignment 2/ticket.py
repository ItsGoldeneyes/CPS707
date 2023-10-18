import logging

RUN = True
LOGIN_TYPE = None

'''
Configure Logging
'''
logging.basicConfig(filename='daily.log',
                     level=logging.INFO,
                     format= "%(message)s")


'''
Helper Functions
'''
def login():
    
    login_loop = True
    while login_loop:
        userid = input("Enter the session type: ", end = "\n\t").lower()
        if userid == "sales":
            LOGIN_TYPE = "sales"
            login_loop = False
        elif userid == "admin":
            LOGIN_TYPE = "admin"
            login_loop = False
        else:
            print("Invalid session type")
    
    password = input("Enter the agent ID: ", end = "\n\t")
    print("Agent ID: ", password)


if __name__ == "__main__":
    while RUN == True:
        command = input("please enter command: ").lower()

        match command:
            case "login":
                login()
            case "logout":
                pass
            # logout()
            case ("exit" | "quit" | "q" | 'x'):
                pass
            # quit()
            case "add":
                pass
                # add()
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

