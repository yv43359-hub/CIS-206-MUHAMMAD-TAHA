# Student Grade Checker

try:
    # #1 Validation checks: Data type and range validation
    score = float(input("Enter your test score (0-100): "))

    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
    else:
        # #3 Nested if statement
        if score >= 60:
            if score >= 90:
                print("You passed with an A!")
            elif score >= 80:
                print("You passed with a B!")
            elif score >= 70:
                print("You passed with a C.")
            else:
                print("You passed with a D.")
        else:
            print("You did not pass.")

# #2 Exception handling
except ValueError:
    print("Invalid input. Please enter a number.")
