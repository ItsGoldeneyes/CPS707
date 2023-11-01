import subprocess
from subprocess import PIPE

RUN_DIR = r'Assignment 2\main.py'

def setup():
    proc = subprocess.Popen(['py', RUN_DIR], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

    def communicate(input_text):
        proc.stdin.write(input_text + '\n')
        proc.stdin.flush()

    def get_output():
        while True:
            output = proc.stdout.readline()
            if output.strip() == "":
                break
            print(output)

    get_output()  # Initial output

    communicate('login')
    get_output()

    communicate('admin')
    get_output()

    communicate('q')
    get_output()

if __name__ == "__main__":
    setup()