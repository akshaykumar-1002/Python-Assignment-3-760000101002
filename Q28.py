# Write a Python program to find the largest and smallest elements in a list.

a=[int(x) for x in input("Enter numbers: ").split()]
if a: print("Largest:",max(a),"Smallest:",min(a))
else: print("List is empty.")
