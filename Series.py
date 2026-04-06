# 30 Days of Python Series - Day 05
# Created by Pavanbhagi

def error_handling_demo():
    print("\n--- Day 5: Problem 1 (Basic Exception Handling) ---")
    try:
        numerator = 100
        denominator = input("Enter a number to divide 100 by: ")
        # Intentional error risk if user types a string or 0
        result = numerator / float(denominator)
        print(f"Result: {result}")
    except ValueError:
        print("Error: You must enter a numerical value.")
    except ZeroDivisionError:
        print("Error: Division by zero is mathematically impossible.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def validation_demo():
    print("\n--- Day 5: Problem 2 (Safe Input Loop) ---")
    while True:
        try:
            age = int(input("Enter your age to continue: "))
            if age < 0:
                print("Age cannot be negative.")
                continue
            print(f"Access Granted. Age verified: {age}")
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        finally:
            print("Check sequence complete.")

if __name__ == "__main__":
    print("Welcome to Day 5 of the 30 Days of Python!")
    error_handling_demo()
    validation_demo()