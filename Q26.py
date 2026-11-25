# Write a Python program to create a list of 10 numbers and display all its elements.

numbers=[]
for i in range(10):
    numbers.append(int(input(f"Enter number {i+1}: ")))
print("List:",numbers)
