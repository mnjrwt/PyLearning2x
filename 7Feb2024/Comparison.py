# Create a program that takes two numbers as input and prints whether the first number is greater than, less than,
# or equal to the second number.

num1 = input("Input first number:")
num2 = input("Input second number:")

n1 = int(num1)
n2 = int(num2)

a1 = (n1 == n2)

a2 = (n1 > n2)

a3 = (n1 < n2)

print("Both numbers are equal :", a1)

print("A is Greater than B :", a2)

print("B is Greater than A :", a3)
