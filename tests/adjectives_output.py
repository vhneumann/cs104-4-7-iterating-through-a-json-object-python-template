import pytest
from common_setup import run_test

def test_adjectives_output():

    # the first parameter is the name of the test file in /tests
    # the second parameter is the name of the test in autograding.json
    # the third parameter is the error message to display if the test fails
    run_test("adjectives_output", "Adjectives Output", "The program doesn't display adjectives for the word or your message doesn't start with 'Adjectives for the word'")

if __name__ == '__main__':
    pytest.main()

