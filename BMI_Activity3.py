def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI using weight in kilograms and height in meters.

    Args:
        weight_kg: The person's weight in kilograms.
        height_m: The person's height in meters.

    Returns:
        The calculated BMI value.
    """
    return weight_kg / (height_m ** 2)


def main():
    """Run the BMI calculator and handle user input."""

    while True:
        weight_input = input(
            "Enter your weight in kilograms (or Q to quit): "
        )

        if weight_input.lower() == "q":
            print("Program ended.")
            break

        try:
            weight_kg = float(weight_input)

            if weight_kg <= 0:
                print("Invalid input. Please enter a positive number.")
                continue

            height_input = input(
                "Enter your height in meters (or Q to quit): "
            )

            if height_input.lower() == "q":
                print("Program ended.")
                break

            height_m = float(height_input)

            if height_m <= 0:
                print("Invalid input. Please enter a positive number.")
                continue

            bmi = calculate_bmi(weight_kg, height_m)

            print("Your BMI is:", round(bmi, 2))

            again = input(
                "Would you like to calculate another BMI? (Y/N): "
            )

            if again.lower() != "y":
                print("Program ended.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()