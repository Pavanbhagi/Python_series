# 30 Days of Python - Day 2
# Topic: String Slicing and Conditionals

def palindrome_checker():
    print("\n--- 1. Palindrome Checker ---")
    user_input = input("Enter a word or phrase: ")
    # Remove spaces and convert to lowercase for accurate checking
    clean_text = user_input.replace(" ", "").lower()
    
    if clean_text == clean_text[::-1]:
        print(f"SUCCESS: '{user_input}' is a palindrome!")
    else:
        print(f"INFO: '{user_input}' is not a palindrome.")

def username_generator():
    print("\n--- 2. Username Generator ---")
    first = input("Enter First Name: ")
    last = input("Enter Last Name: ")
    year = input("Enter Birth Year (YYYY): ")
    
    # Logic: First 3 letters of first name + full last name + last 2 digits of year
    username = f"{first[:3].lower()}_{last.lower()}{year[-2:]}"
    print(f"Your New Username: {username}")

def main():
    palindrome_checker()
    username_generator()
    print("\nDay 2 Complete!")

if __name__ == "__main__":
    main()