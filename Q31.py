# Write a Python program to insert an element at a specified position in a list.

a=[int(x) for x in input("Enter list elements: ").split()]
v=int(input("Value to insert: "))
p=int(input("Index position: "))
if 0<=p<=len(a):
    a.insert(p,v)
    print(a)
else: print("Invalid position.")
