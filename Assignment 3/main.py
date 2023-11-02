from subprocess import Popen, PIPE, STDOUT

RUN_DIR = r'..\Assignment 2\main.py'

greeting = "Please enter command: "
loginout = "Enter the session type: "+greeting
logoutout = "You have been logged out.\n"
quitout = "Exiting program...\n"
eventout = "Enter event name: " 
dateout = "Enter event date YYYYMMDD: " 
qtyout = "Enter number of tickets: "
addconfirm = "Event added successfully\n"+greeting
badqty = "Invalid quantity entered\n"+greeting
badprivout = "You must be admin\n"
baddeletetout = "Event not found or cannot delete tickets from it."
exitout = "Exiting program...\n"

TESTS = {
    "login": {
        "login_sales": {
            "input": ["login", "sales", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
        "login_admin": {
            "input": ["login", "admin", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
        "login_restricted": {
            "input": ["add", "q"],
            "expected_output": "Please enter command: " +
                                "You are not logged in, please 'login' to continue\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
        "login_bad": {
            "input": ["login", "bad", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Invalid session type. Please enter admin or sales\n" +
                                "Please enter command: "
                                "Exiting program...\n"
        },
        "login_restricted": {
            "input": ["login", "admin", "login", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "You are already logged in\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        }
    },
    "logout": {
        "logout_success": {
            "input": ["login", "admin", "logout", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "You have been logged out.\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
        "logout_nologin": {
            "input": ["logout", "q"],
            "expected_output": "Please enter command: " +
                                "You are not logged in, please 'login' to continue\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
        "logout_transaction_file": {
            "input": ["login", "admin", "logout", "login", "admin", "transaction", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "You have been logged out.\n" +
                                "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "00\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
    },
    "create_event": {
        "create_event_success": {
            "input": ["login", "admin", "create", "Event1", "20231129", "100", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Enter event name: " +
                                "Enter event date (YYYYMMDD): " +
                                "Enter number of tickets: "
                                "Event created successfully.\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
            
        },
        "create_event_noadmin": {
            "input": ["login", "sales", "create", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "You are not authorized to create events.\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
        "create_event_datefail": {
            "input": ["login", "admin", "create", "Event1", "20231002", "100", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Enter event name: " +
                                "Enter event date (YYYYMMDD): " +
                                "Enter number of tickets: "
                                "Event date must be between tomorrow and 2 years from today.\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
        "create_event_namefaillength": {
            "input": ["login", "admin", "create", "Event1"*100, "20231129", "100", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Enter event name: " +
                                "Enter event date (YYYYMMDD): " +
                                "Enter number of tickets: "
                                "Event name must be less than or equal to 15 characters.\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
        "create_event_namefailcopy": {
            "input": ["login", "admin", "create", "Event1", "20231129", "100", "create", "Event1", "20231129", "100", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Enter event name: " +
                                "Enter event date (YYYYMMDD): " +
                                "Enter number of tickets: "
                                "Event created successfully.\n" +
                                "Please enter command: " +
                                "Enter event name: " +
                                "Enter event date (YYYYMMDD): " +
                                "Enter number of tickets: "
                                "Event already exists.\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
        "create_event_eventtransactioncheck": {
            "input": ["login", "admin", "create", "Event1", "20231129", "100", "logout", "login", "admin", "transaction", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Enter event name: " +
                                "Enter event date (YYYYMMDD): " +
                                "Enter number of tickets: "
                                "Event created successfully.\n" +
                                "Please enter command: " +
                                "You have been logged out.\n" +
                                "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "03 Event1_________ 20231129 0100\n" +
                                "00\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
    },
    "add": {
        "add_input": {
            "input": ["login", "admin", "add", "Event1", "20231129", "100" , "q"],
            "expected_output": greeting + loginout + eventout + dateout + qtyout + addconfirm + exitout
        },
        "add_eventlog": {
            "input": ["login", "admin", "add", "Event1", "20231129", "100", "logout", "login", "admin", "transaction", "q"],
            "expected_output": greeting + loginout + eventout + dateout + qtyout + addconfirm + logoutout + 
            "05 Event1_________ 20231129 0300\n" + exitout
        },
        "add_nologin":{
            "input" :["login", "sales", "add", "q"],
            "expected_output": greeting + loginout + badprivout + greeting +exitout
        },
        "add_bad_qty" :{
            "input" : ["login", "admin", "add", "Event1", "20231129", "-1" , 'q'],
            "expected_output": greeting + loginout + eventout + dateout + qtyout + badqty + exitout
        },
        "add_bad_qty_type" :{
            "input" : ["login", "admin", "add", "Event1", "20231129", "string" , 'q'],
            "expected_output": greeting + loginout + eventout + dateout + qtyout + badqty + exitout
        }  
    },
    "delete" :{
        "delete_tickets" : {
            "input" : ["login", "admin", "delete", "Event1", "10", "yes" , 'q'],
            "expected_output": greeting + loginout + eventout + qtyout + 
            "Are you sure you want to delete 10 tickets from the event Event1? (yes/no): " +
            "Ticket: 10 deleted successfully from event Event1\n" +
            greeting + exitout
        },

        "delete_ticket_transaction" : {
            "input" : ["login", "admin", "delete", "Event1", "10", "yes","transaction","q"],
            "expected_output": greeting + loginout + eventout + qtyout + 
            "Are you sure you want to delete 10 tickets from the event Event1? (yes/no): " +
            "Ticket: 10 deleted successfully from event Event1\n" + greeting+
            "05 Event1_________ 20231129 0010\n"+ exitout
        },
        "delete_no_admin" : {
            "input" : ["login", "sales", "delete", "q"],
            "expected_output": greeting + loginout + badprivout + greeting +exitout
        },
        "delete_wrong_event" : {
            "input" : ["login", "admin", "delete", "BadEvent", "q"],
            "expected_output": greeting + loginout + eventout + baddeletetout + exitout
        },
        "delete_bad_quantity" : {
            "input" : ["login", "admin", "delete", "Event1", "-1" , 'q'],
            "expected_output": greeting + loginout + eventout + qtyout + badqty +exitout 
        },
    }
       
}



def runTest(input, test_name, expected_output):
    print(f"Running {test_name} test...")
    proc = Popen(['py', RUN_DIR], stdout=PIPE, stdin=PIPE, stderr=STDOUT, text=True)
    output, error = proc.communicate("\n".join(input))
    
    if error:
        print(f"{test_name} test failed!")
        print(f"Error: {error}")
        return
    
    if output == expected_output:
        print(f"{test_name} test passed!")
    else:
        print(f"{test_name} test failed!")
        print(f"Expected output: \t{expected_output}")
        print(f"Actual output: \t\t{output}")
    print("-"*50)
    
    
    
if __name__ == "__main__":
    print("Running tests...")
    for test_suite in TESTS:
        print(f"Running {test_suite} test suite...")
        print("="*75)
        for test in TESTS[test_suite]:
            runTest(TESTS[test_suite][test]["input"], test, TESTS[test_suite][test]["expected_output"])

    