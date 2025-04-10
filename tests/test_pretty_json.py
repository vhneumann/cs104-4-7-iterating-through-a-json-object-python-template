# *****************************************************************************
# *                                                                           *
# *   IMPORTANT: DO NOT MODIFY THIS FILE                                      *
# *                                                                           *
# *   This testing file is provided to help you check the functionality of    *
# *   your code and understand the requirements for this assignment.          *
# *                                                                           *
# *   Please review the tests carefully to understand what is expected, but   *
# *   DO NOT make any changes to this file. Modifying this file will          *
# *   interfere with the grading system, lead to incorrect results, and       *
# *   will be flagged as cheating.                                            *
# *                                                                           *
# *   Focus on writing your own code to meet the requirements outlined in the *
# *   tests.                                                                  *
# *                                                                           *
# *****************************************************************************

import subprocess
import pytest
from common_setup import pre_test_setup, check_internet_connection

# Global variables
test_outputs = {}
test_name = None
test_points_awarded = {}
test_response_data = {}

# Cost estimate for API calls
# - 1,233 tokens for gtp-4o model costs $2.50 per 1M tokens, approx. $0.004 per run.
# - GitHub running tests separately will call the API 8 times, costing about $0.032 per push.

def test_all():
    """
    Run all tests to ensure the program meets the assignment requirements.
    """
    # Setup pre-test environment
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup()

    # Check internet connection
    if check_internet_connection():
        # Verify all points are awarded
        assert (
            test_response_data['totalPointsAwarded'] == test_response_data['totalPointsPossible']
        ), test_feedback
    else:
        # Test adjective output when offline
        output = test_outputs["adjectives_output"]
        adjectives = output.split(",")
        assert len(adjectives) > 2, (
            "The program doesn't display adjectives for the word separated by commas"
        )

        # Test pretty_json.py execution
        result = subprocess.run(
            ['python3', 'pretty_json.py'], capture_output=True, text=True
        )
        assert result.returncode == 0, (
            "The program did not finish successfully. "
            "Please review code for any errors that would prohibit the program from executing completely"
        )


if __name__ == '__main__':
    pytest.main()
