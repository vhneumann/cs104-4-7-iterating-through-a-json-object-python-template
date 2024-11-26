# common_setup.py
import subprocess
import requests
import json
import socket
import os


def check_internet_connection():
    """Check if there is an active internet connection."""
    try:
        # Try to connect to a known server (Google's public DNS server)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False


def run_program():
    """Run the student's program using subprocess and return the output."""

    # Run the student's program and capture output
    result = subprocess.run(
        ['python3', 'pretty_json.py'],  # Adjust this command if using a different Python version or path
        text=True,
        capture_output=True,
        check=True  # If check is True and the exit code was non-zero, it raises a
        # CalledProcessError. The CalledProcessError object will have the return code
        # in the returncode attribute, and output & stderr attributes if those streams
        # were captured.
    )

    return result.stdout  # Capture standard output


def logic_adjectives_output():
    """Logic to test if the program displays adjectives output."""
    output = run_program()
    return output

def logic_program_finishes():
    """Logic to test if the program finishes successfully."""
    output = run_program()
    return output

def pre_test_setup(test_name=None):
    test_outputs = {}
    test_points_awarded = {}
    test_feedback = {}

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
            with open('./tests/test_pretty_json.py', 'r') as f:
                pytest_code = f.read()
            with open('.github/classroom/autograding.json', 'r') as f:
                autograding_config = json.load(f)

            # Determine which test is being run
            if test_name:
                print(f"Running test: {test_name}")
                # Filter the autograding config to include only the relevant section - this avoids grading on unnecessary criteria
                relevant_tests = [test for test in autograding_config["tests"] if f"/{test_name}.py" in test["run"]]
                autograding_config["tests"] = relevant_tests
            # print('Autograding Config: '+json.dumps(autograding_config))

            # Prepare the data for the POST request
            data = {
                "studentCode": student_code,
                "pytestCode": pytest_code,
                "autogradingConfig": json.dumps(autograding_config),
                "terminalOutputs": list(test_outputs.values())
            }

            # Send the POST request
            response = requests.post('https://autograding-api-next.vercel.app/api/autograde', json=data)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Parse the response
            test_response_data = response.json()

            # Store the points awarded for each test
            test_points_awarded.update({test['name']: test['pointsAwarded'] for test in test_response_data["tests"]})

        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"API call failed: {e}")
            print(
                "Proceeding without API response. Run the test again with a working API to receive more user-friendly feedback.")

    if check_internet_connection() and test_response_data:
        # Print the results in a well-formatted manner
        test_feedback = (
                "\nTest Results:\n"
                + "\n".join(
            [
                f"Test Name: {test['name']}\nPoints Awarded: {test['pointsAwarded']}\nFeedback: {test['feedback']}\n"
                for test in test_response_data["tests"]
            ]
        )
                + f"\nTotal Points Awarded: {test_response_data['totalPointsAwarded']}\n"
                + f"Total Points Possible: {test_response_data['totalPointsPossible']}\n"
                + "\nSpecific Code Feedback:\n"
                + "\n".join(
            [
                f"Line {feedback['line']}: {feedback['feedback']}\nRecommendation: {feedback['recommendation']}\n"
                for feedback in test_response_data["specificCodeFeedback"]["code"]
            ]
        )
                + "\nGeneral Feedback:\n"
                + test_response_data["specificCodeFeedback"]["general"]
        )

    else:
        print(
            "No active internet connection or API response. Run the test again with an active internet connection and a working API to receive more user-friendly feedback.")

    return test_outputs, test_points_awarded, test_feedback, test_response_data


def run_test(test_name, test_point_key, offline_feedback):
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup(test_name=test_name)
    output = test_outputs[test_name]

    # Load points from autograding.json
    with open('.github/classroom/autograding.json', 'r') as f:
        autograding_config = json.load(f)

    # Find the points for the specific test
    test_config = next((test for test in autograding_config["tests"] if test["name"] == test_point_key), None)
    expected_points = test_config["points"] if test_config else 0

    if check_internet_connection():
        assert test_points_awarded.get(test_point_key, 0) == expected_points, test_feedback
    else:
        assert offline_feedback in output.strip(), offline_feedback