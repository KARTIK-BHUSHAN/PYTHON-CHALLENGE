 Day 1: Basics of Python Programming
🧠 Topics Covered:
🔸 Print Statements
Use print() to display messages or values.
print("Hello, world")

🔸 Variables
Store values using variables:
a = "jakidada"
b = "hakka noodle"
c = 798
e = 798.588


🔸 Input from User
input() collects input as string.
split() divides input into multiple values.

name = input("Enter your name: ")
student1, student2 = input("Enter two names: ").split()

🔸 Type Conversion
Convert input using int() or float():

age = int(input("Enter your age: "))


🔸 Conditional Statements

if age < 18:
    print("Under 18")
elif 18 <= age < 50:
    print("18+")
else:
    print("Too old for that")


🔸 Checking Data Types
print(type(age))  # <class 'int'>


🔸 Print Formatting with sep and end
print("Hello", name, end=" >>> ")
print("joined the class")
print("Name", "Score", sep=" --- ")


🔸 Mini Project: Compare Scores
Input two students’ names and scores
Display welcome message
Compare scores and print who scored higher
Show their email IDs
