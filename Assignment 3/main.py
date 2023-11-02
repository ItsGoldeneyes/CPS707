from subprocess import Popen, PIPE, STDOUT

RUN_DIR = r'Assignment 2\main.py'

TESTS = {
    "login_admin": {
        "input": ["login", "admin", "q"],
        "expected_output": "please enter command: \
                            Enter the session type: \
                            please enter command: \
                            Exiting program...\n"
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
        print(f"Expected output: {expected_output}")
        print(f"Actual output: {output}")
    print("--------------------------------------------------")
    
    
    
if __name__ == "__main__":
    print("Running tests...")
    print("--------------------------------------------------")
    for test in TESTS:
        runTest(TESTS[test]["input"], test, TESTS[test]["expected_output"])

    