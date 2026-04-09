# 30 Days of Python - Master Script (Days 1-6)
# Created by Pavanbhagi

def day_1_basics():
    print("Day 1: Hello Python!")

def day_2_strings():
    text = "Python"
    print(f"Day 2: Reversed string is {text[::-1]}")

def day_3_lists():
    nums = [1, 2, 3]
    print(f"Day 3: List doubled -> {[x*2 for x in nums]}")

def day_4_dicts():
    user = {"name": "Pavan", "day": 4}
    print(f"Day 4: User name is {user.get('name')}")

def day_5_exceptions():
    print("Day 5: Error Handling...")
    try:
        res = 10 / 0
    except ZeroDivisionError:
        print("Handled Zero Division Error successfully.")

def day_6_files():
    print("Day 6: File Handling...")
    filename = "pavan_series.txt"
    with open(filename, "w") as f:
        f.write("Learning File I/O on Day 6.")
    
    with open(filename, "r") as f:
        print(f"File content: {f.read()}")

if __name__ == "__main__":
    print("--- 30 DAYS OF PYTHON SERIES ---")
    day_1_basics()
    day_2_strings()
    day_3_lists()
    day_4_dicts()
    day_5_exceptions()
    day_6_files()