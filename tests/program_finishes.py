import pytest
from common_setup import run_test

def test_program_finishes():

    # the first parameter is the name of the test file in /tests
    # the second parameter is the name of the test in autograding.json
    # the third parameter is the error message to display if the test fails
    run_test("program_finishes", "The program finishes", "The program did not finish successfully. Please review code for any errors that would prohibit the program from executing completely")

if __name__ == '__main__':
    pytest.main()