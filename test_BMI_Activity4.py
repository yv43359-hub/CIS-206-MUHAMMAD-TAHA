import unittest
import subprocess
import sys
from pathlib import Path


PROGRAM = Path(__file__).with_name("BMI_Activity4.py")


class TestBMIProgram(unittest.TestCase):

    def run_program(self, user_input):
        result = subprocess.run(
            [sys.executable, str(PROGRAM)],
            input=user_input,
            text=True,
            capture_output=True
        )
        return result.stdout

    def test_valid_bmi_calculation(self):
        output = self.run_program("70\n1.75\nn\n")
        self.assertIn("Your BMI is: 22.86", output)

    def test_negative_weight(self):
        output = self.run_program("-5\n70\n1.75\nn\n")
        self.assertIn("Invalid input. Please try again.", output)

    def test_non_numeric_weight(self):
        output = self.run_program("abc\n70\n1.75\nn\n")
        self.assertIn("Invalid input. Please enter a number.", output)

    def test_quit_option(self):
        output = self.run_program("q\n")
        self.assertIn("Program ended.", output)


if __name__ == "__main__":
    unittest.main()