# common_setup.py
import subprocess
import requests
import json
import socket
import os
import platform
import sys
sys.path.append('..')
from central_setup.central_setup import (
    execute_logic,
    check_internet_connection,
    run_program,
    run_single_test,  # this function is called by the test files that import it from this file: common_setup.py
)

program_name = 'pretty_json.py'

def run_test(test_name, test_description, error_message):
    run_single_test(test_name, test_description, error_message, pre_test_setup)

# Test functions for JSON iteration
def logic_adjectives_output():
    """Test if the program correctly extracts and formats adjectives from JSON."""
    return run_program([], program_name)

def logic_program_finishes():
    """Test if the program completes successfully."""
    return run_program([], program_name)

def pre_test_setup(test_name=None):
    test_outputs = {}
    test_points_awarded = {}
    test_feedback = ""
    test_response_data = None

    if test_name:
        if test_name == "adjectives_output":
            test_outputs["adjectives_output"] = logic_adjectives_output()
        elif test_name == "program_finishes":
            test_outputs["program_finishes"] = logic_program_finishes()
    else:
        test_outputs = {
            "adjectives_output": logic_adjectives_output(),
            "program_finishes": logic_program_finishes()
        }

    if check_internet_connection():
        try:
            # Read the contents of the files
            with open('pretty_json.py', 'r') as f:
                student_code = f.read()
            with open('tests/test_pretty_json.py', 'r') as f:
                pytest_code = f.read()
            with open('.github/classroom/autograding.json', 'r') as f:
                autograding_config = json.load(f)

            # Pass the logic to the central_setup module
            test_outputs, test_points_awarded, test_feedback, test_response_data = execute_logic(
                test_name, test_outputs, student_code, pytest_code, autograding_config
            )

        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"API call failed: {e}")
            print("Proceeding without API response. Run the test again with a working API to receive more user-friendly feedback.")

    return test_outputs, test_points_awarded, test_feedback, test_response_data