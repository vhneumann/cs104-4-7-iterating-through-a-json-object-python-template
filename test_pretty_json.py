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


import io
import subprocess
import sys
import unittest
import pretty_json  # Import the module to be tested

class TestAdjectivesOutput(unittest.TestCase):
    def test_adjectives_output(self):
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function or code block from pretty_json.py
        pretty_json.main()  # Assuming the main code is encapsulated in a main() function

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Get output and verify
        output = captured_output.getvalue().strip()
        self.assertIn("Adjectives for the word", output)

    def test_program_finishes(self):
        result = subprocess.run(['python', 'pretty_json.py'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, msg="The program did not finish successfully")



if __name__ == '__main__':
    unittest.main()
