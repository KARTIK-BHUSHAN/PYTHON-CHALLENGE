# Day 1 - Python Basics by Kritarth

# --- Print Statements ---
print("Hello, world")  # First Python program

# --- Variable Initialization ---
a = "jakidada"
b = "hakka noodle"
c = 798
e = 798.588

# --- Print Variables ---
print(a)
print(b)
print(c)
print(e)

# --- Taking Input from User ---
name = input("Type your name: ")
print("Hello!", name, "Welcome to CodeWithKartik")

# --- Taking Multiple Inputs ---
student1, student2 = input("Write the names of two students: ").split()
print(student1)
print(student2)

# --- Conditional Input Handling ---
age = int(input("Enter the age of one student: "))
if age < 18:
    print("You are under 18")
elif 18 <= age < 50:
    print("You are 18+")
else:
    print("Too old for that")

# --- Checking Data Types ---
print("The data type of 'age' is:", type(age))

# --- Extra Variables for Practice ---
a = 3563
b = "rohit"
c = "sushma"
d = "lolita"
r = 5873.83

# --- Using 'end' and 'sep' in print() ---
print(b, end="@gmail.com\n")
print(b, r, sep=" ")

# --- Summary Task: Compare Two Students’ Scores ---
name1, name2 = input("Name both students >>> ").split()
score1, score2 = map(int, input("Score both students >>> ").split())

print(f"Hello! {name1} and {name2}, Welcome!")
print(f"Type of score1: {type(score1)}, Type of score2: {type(score2)}")

# Compare the scores
if score1 > score2:
    print(f"{name1} scored more than {name2}")
elif score2 > score1:
    print(f"{name2} scored more than {name1}")
else:
    print("Both scored the same!")

# --- Display Email IDs using print formatting ---
print("Email ID of", name1, "is", sep="---", end=" >>> ")
print(name1 + "@gmail.com")

print("Email ID of", name2, "is", sep="---", end=" >>> ")
print(name2 + "@gmail.com")
