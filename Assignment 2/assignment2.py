# BMI Calculator
# Student: Muhammad Taha

def calculate_bmi(weight_kg, height_m):
    """Calculate BMI using weight in kilograms and height in meters."""
    return weight_kg / (height_m ** 2)


weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight_kg, height_m)

print("Your BMI is:", round(bmi, 2))