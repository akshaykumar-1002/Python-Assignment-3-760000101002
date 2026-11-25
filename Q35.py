# Write a Python program to sort a list in ascending and descending order.

a=[int(x) for x in input("Enter numbers: ").split()]
print("Ascending:",sorted(a))
print("Descending:",sorted(a,reverse=True))
