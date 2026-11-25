# Write a Python program to demonstrate list slicing with different index ranges.

a=[int(x) for x in input("Enter list elements: ").split()]
print("Full list:",a)
print("First three:",a[:3])
print("From index 2:",a[2:])
print("Index 1 to 4:",a[1:5])
print("Every second:",a[::2])
