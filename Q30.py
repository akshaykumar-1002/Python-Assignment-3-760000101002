# Write a Python program to count the number of even and odd elements in a list.

a=[int(x) for x in input("Enter integers: ").split()]
print("Even:",sum(1 for x in a if x%2==0))
print("Odd:",sum(1 for x in a if x%2!=0))
