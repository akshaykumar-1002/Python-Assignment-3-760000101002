# Write a Python program to count the frequency of a given element in a list.

a=[int(x) for x in input("Enter list elements: ").split()]
v=int(input("Element to count: "))
print("Frequency:",a.count(v))
