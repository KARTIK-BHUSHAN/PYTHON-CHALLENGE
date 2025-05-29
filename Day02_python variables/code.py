# Variable 'x' stores the integer value 10
x = 5

# Variable 'name' stores the string "Samantha"
name = "Samantha"  

print(x)
print(name)

# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)  
print(f)  
print(s2)

def f():
    a = "I am local"
    print(a)

f()
# print(a)  # This would raise an error since 'local_var' is not accessible outside the function

a = "I am global"

def f():
    global a
    a = "Modified globally"
    print(a)

f()
print(a)

# Assigning value to variable
x = 10
print(x) 

# Removing the variable using del
del x

# Trying to print x after deletion will raise an error
# print(x)  # Uncommenting this line will raise NameError: name 'x' is not defined

a, b = 5, 10
a, b = b, a
print(a, b)

word = "Python"
length = len(word)
print("Length of the word:", length)
