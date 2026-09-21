def calculate_bmi(weight_kg, height_m):
    """Calculate BMI using kilograms and meters."""
    return weight_kg / (height_m ** 2)


def pounds_to_kg(weight_lb):
    """Convert pounds to kilograms."""
    return weight_lb * 0.453592


def inches_to_meters(height_in):
    """Convert inches to meters."""
    return height_in * 0.0254


while True:
    weight = input("Enter your weight in kilograms (or Q to quit): ")

    if weight.lower() == "q":
        break

    try:
        weight_kg = float(weight)

        if weight_kg <= 0:
            print("Invalid input. Please try again.")
            continue

        height = input("Enter your height in meters (or Q to quit): ")

        if height.lower() == "q":
            break

        height_m = float(height)

        if height_m <= 0:
            print("Invalid input. Please try again.")
            continue

        bmi = calculate_bmi(weight_kg, height_m)

        print("Your BMI is:", round(bmi, 2))

        again = input("Would you like to calculate another BMI? (Y/N): ")

        if again.lower() != "y":
            break

    except ValueError:
        print("Invalid input. Please enter a number.")


print("\nBMI Table")
print("Weight", end="")

for height in range(58, 77, 2):
    print(f"{height:>8}", end="")

print()

for weight in range(100, 251, 10):
    print(f"{weight:>6}", end="")

    for height in range(58, 77, 2):
        weight_kg = pounds_to_kg(weight)
        height_m = inches_to_meters(height)

        bmi = calculate_bmi(weight_kg, height_m)

        print(f"{bmi:>8.1f}", end="")

    print()

print("\nProgram ended.")