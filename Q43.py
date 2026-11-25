# Write a Python program to find the index of a specified element in a list.

a=[int(x) for x in input("Enter list elements: ").split()]
v=int(input("Element to find: "))
if v in a: print("Index:",a.index(v))
else: print("Element not found.")
