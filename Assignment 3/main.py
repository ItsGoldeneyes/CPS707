from subprocess import Popen, PIPE, STDOUT

RUN_DIR = r'Assignment 2\main.py'

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
                                "You have been logged out\n" +
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
                                "You have been logged out\n" +
                                "Please enter command: " +
                                "Enter the session type: " +
                                "Please enter command: " +
                                "00\n" +
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

    