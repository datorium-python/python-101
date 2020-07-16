# Simple Data Types
# number -> int, float
# string

greeting = "Hello, from Variables!"

name = "Andrew"
year = 1988

# YYYY-MM-DD
year_now = 2020
date = "2020-10-18"

print("")
print(greeting)
print("Name: ", name)
print("Age: ", year_now - year)

# Basic Operations with Numbers
# + - / * ** // %
a = 10
b = 2.3
print("Add: ", a + b)
print("Subtract: ", a - b)
print("Divide: ", a / b)
print(a * b)
print(a ** b)
print(a // b)
print(a % b)

result = b
result = result + a
result += a
result -= a
result *= a
result /= a
print(result)

# Odd and Even
print("")
print("Odd and Even")
print(0 % 2)
print(1 % 2)
print(2 % 2)
print(3 % 2)
print(4 % 2)

# Strings
print("")
print("Strings")
print(name * 10)
print(name.upper())
print(name.lower())
print(name.endswith('Python'))
print(name.endswith('w'))
print(name.isdigit())
number = "103"
print(number.isdigit())
print(int(number))
print(number.isalnum())
print(number.isalpha())
print(greeting.title())
print(greeting.capitalize())
# name.example  # property
# name.example()  # method / function
