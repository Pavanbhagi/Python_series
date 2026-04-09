# 30 Days of Python - Master Script (Days 1-7)
# Created by Pavanbhagi

class PythonSeries:
    def __init__(self, username):
        self.username = username
        self.progress = 7

    def day_7_oop(self):
        print(f"Day 7: {self.username} is learning Object-Oriented Programming!")

def day_1_basics():
    print("Day 1: Hello Python!")

def day_2_strings():
    print(f"Day 2: Reversed string -> {'Python'[::-1]}")

def day_3_lists():
    print(f"Day 3: Squares -> {[x*x for x in range(5)]}")

def day_4_dicts():
    print(f"Day 4: Dict access -> {'Success'}")

def day_5_exceptions():
    try:
        1/0
    except ZeroDivisionError:
        print("Day 5: Exception Handled.")

def day_6_files():
    with open("temp.txt", "w") as f:
        f.write("Day 6 Data")
    print("Day 6: File I/O Success.")

if __name__ == "__main__":
    print("--- 30 DAYS OF PYTHON SERIES ---")
    day_1_basics()
    day_2_strings()
    day_3_lists()
    day_4_dicts()
    day_5_exceptions()
    day_6_files()
    
    # OOP Implementation for Day 7
    series = PythonSeries("Pavan")
    series.day_7_oop()