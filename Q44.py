# Write a Python program to copy one list into another and demonstrate the difference between copy() and direct assignment.

a=[int(x) for x in input("Enter list elements: ").split()]
direct=a
copied=a.copy()
a.append(100)
print("Original:",a)
print("Direct assignment:",direct)
print("Using copy():",copied)
