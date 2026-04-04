# 30 Days of Python Series - Day 3
# Topic: Lists, Loops, and Data Cleaning

def filter_priority_tasks():
    """Demonstrates List Comprehension for filtering"""
    print("\n--- Problem 1: Priority Task Filter ---")
    tasks = [
        "Setup Server (High)", 
        "Change Header Color", 
        "Database Migration (High)", 
        "Write Documentation"
    ]
    
    # Pythonic way to filter lists
    urgent_tasks = [t for t in tasks if "(High)" in t]
    
    print(f"All Tasks: {tasks}")
    print(f"Urgent Filtered: {urgent_tasks}")

def clean_numerical_data():
    """Demonstrates Sets for duplicate removal and sorting"""
    print("\n--- Problem 2: Data Cleaner ---")
    raw_user_ids = [102, 304, 102, 506, 304, 900, 102]
    
    # set() removes duplicates, sorted() puts them in order
    unique_ids = sorted(list(set(raw_user_ids)))
    
    print(f"Raw Input: {raw_user_ids}")
    print(f"Cleaned IDs: {unique_ids}")

def main():
    print("Welcome to Day 3 of the Python Series!")
    filter_priority_tasks()
    clean_numerical_data()
    print("\nSession Complete. Ready for Day 4!")

if __name__ == "__main__":
    main()