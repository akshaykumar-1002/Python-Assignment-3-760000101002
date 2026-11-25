# Write a Python program to delete an element from a list using the remove() method.

a=[int(x) for x in input("Enter list elements: ").split()]
v=int(input("Element to remove: "))
if v in a: a.remove(v)
else: print("Element not found.")
print(a)
