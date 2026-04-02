# 30 Days of Python - Day 1
# Topic: Variables, Inputs, and Functions

def main():
    print("--- Simple Interest Calculator ---")
    
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (%): "))
        time = float(input("Enter the time in years: "))

        interest = (principal * rate * time) / 100
        total = principal + interest

        print(f"\nResults:")
        print(f"Interest Earned: {interest:.2f}")
        print(f"Total Balance: {total:.2f}")
        
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()