from subprocess import Popen, PIPE, STDOUT

RUN_DIR = r'Assignment 5\main.py'

TESTS = {
    "delete" :{
        "delete_tickets" : {
            "input" : ["login", "admin", "delete", "Star_Wars______", "10", "yes" , 'q'],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Enter event name: " +
                                "Enter number of tickets: " +
                                "Are you sure you want to delete 10 tickets from the event Star_Wars______? (yes/no): " +
                                "Ticket: 10 deleted successfully from event Star_Wars______\n" +
                                "Please enter command: " +
                                "Exiting program...\n"       
        },
        "delete_ticket_transaction" : {
            "input" : ["login", "admin", "delete", "Star_Wars______", "10", "yes","logout","login", "sales","transaction","q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Enter event name: " +
                                "Enter number of tickets: " +
                                "Are you sure you want to delete 10 tickets from the event Star_Wars______? (yes/no): " +
                                "Ticket: 10 deleted successfully from event Star_Wars______\n" + 
                                "Please enter command: " +
                                "You have been logged out.\n" +
                                "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "05_Star_Wars_______10\n" + 
                                "00\n" +
                                "Please enter command: " +
                                "Exiting program...\n"       
        },
        "delete_no_admin" : {
            "input" : ["login", "sales", "delete", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "You must be admin\n" +
                                "Please enter command: " +
                                "Exiting program...\n"       
        },
        "delete_wrong_event" : {
            "input" : ["login", "admin", "delete", "BadEvent", "q"],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Enter event name: " +
                                "Event not found or cannot delete tickets from it.\n" + 
                                "Please enter command: " +
                                "Exiting program...\n"       
        },
        "delete_bad_quantity" : {
            "input" : ["login", "admin", "delete", "Star_Wars______", "-1" , 'q'],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "Enter event name: " +
                                "Enter number of tickets: " +
                                "Invalid quantity entered\n" +
                                "Please enter command: " +
                                "Exiting program...\n"        
        },
    },
    "sell" : {
        "sell_success" : {
            "input" : ["login", "admin", "sell", "Star Wars", "10", 'q'],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " + 
                                "Enter event name: " +
                                "Enter number of tickets: " +
                                "10 tickets sold from event Star Wars.\n" +
                                "Please enter command: " +
                                "Exiting program...\n"       
        },
        "sell_invalid_event" : {
            "input" : ["login", "admin", "sell", "BadEvent", "10", 'q'],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " + 
                                "Enter event name: " +
                                "Enter number of tickets: " +
                                "Event does not exist.\n" +
                                "Please enter command: " +
                                "Exiting program...\n"
        },
        "sell_too_many_tickets_sales" : {
            "input" : ["login", "sales", "sell", "Star Wars", "1000", 'q'],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " + 
                                "Enter event name: " +
                                "Enter number of tickets: " +
                                "Not enough tickets available.\n" +
                                "Please enter command: " +
                                "Exiting program...\n"       
        },
        "sell_not_too_many_tickets_sales" : {
            "input" : ["login", "admin", "sell", "Star Wars", "999", 'q'],
            "expected_output": "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " + 
                                "Enter event name: " +
                                "Enter number of tickets: " +
                                "999 tickets sold from event Star Wars.\n" +
                                "Please enter command: " +
                                "Exiting program...\n"       
        },
                       
    },
       
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

    