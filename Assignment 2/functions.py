def login():
    userid = input("enter user ID: ")
    password = input("enter password: ")
    print(userid, password)

def logout():
    print("logout")

def add():
    transaction_code = "01"
    event_name = input("enter event name: ")
    event_date = input('enter event date YYYYMMDD: ')
    num_tickets = input("enter number of tickets: ")
    event_transaction = "{}_{}_{}_{}".format(transaction_code,event_name,event_date,num_tickets)
    #print("transaction added: ", event_transaction)
    return event_transaction