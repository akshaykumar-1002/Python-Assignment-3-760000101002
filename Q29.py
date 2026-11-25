# Write a Python program to calculate the sum and average of all elements in a list.

a=[float(x) for x in input("Enter numbers: ").split()]
if a: print("Sum:",sum(a),"Average:",sum(a)/len(a))
else: print("List is empty.")
