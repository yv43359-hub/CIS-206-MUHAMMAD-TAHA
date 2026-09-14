# Group Assignment 1 - BMI Calculator
# Student: Muhammad Taha
#
# Coding standards applied:
# 1. Variables use descriptive snake_case names.
# 2. Function names use descriptive snake_case.
# 3. Constants use uppercase names with underscores.
# 4. Functions are documented with docstrings.
# 5. Comments explain how the coding standards are applied.

POUNDS_TO_KG = 0.453592
FEET_TO_METERS = 0.3048
INCHES_TO_METERS = 0.0254


def get_weight():
    """Get the user's weight in pounds."""
    weight_pounds = float(input("Enter your weight in pounds: "))
    return weight_pounds


def get_height():
    """Get the user's height in feet and inches."""
    height_feet = int(input("Enter your height in feet: "))
    height_inches = int(input("Enter your additional inches: "))
    return height_feet, height_inches


def convert_weight(weight_pounds):
    """Convert weight from pounds to kilograms."""
    weight_kg = weight_pounds * POUNDS_TO_KG
    return weight_kg


def convert_height(height_feet, height_inches):
    """Convert height from feet and inches to meters."""
    height_m = (height_feet * FEET_TO_METERS) + (
        height_inches * INCHES_TO_METERS
    )
    return height_m


def calculate_bmi(weight_kg, height_m):
    """Calculate and return BMI."""
    bmi = weight_kg / (height_m ** 2)
    return bmi


def display_result(bmi):
    """Display BMI and the recommended BMI categories."""
    print(f"Your BMI is: {bmi:.1f}")

    print("\nBMI Categories:")
    print("Underweight: Below 18.5")
    print("Normal weight: 18.5 - 24.9")
    print("Overweight: 25.0 - 29.9")
    print("Obesity: 30.0 or higher")

    if bmi < 18.5:
        print("Your category: Underweight")
    elif bmi < 25:
        print("Your category: Normal weight")
    elif bmi < 30:
        print("Your category: Overweight")
    else:
        print("Your category: Obesity")


def main():
    """Run the BMI calculator."""
    weight_pounds = get_weight()
    height_feet, height_inches = get_height()

    weight_kg = convert_weight(weight_pounds)
    height_m = convert_height(height_feet, height_inches)

    bmi = calculate_bmi(weight_kg, height_m)

    display_result(bmi)


main()