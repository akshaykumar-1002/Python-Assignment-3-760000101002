# Write a Python program to create two sets and perform union, intersection, difference and symmetric difference operations.

a=set(input("First set elements separated by spaces: ").split())
b=set(input("Second set elements separated by spaces: ").split())
print("Union:",a|b)
print("Intersection:",a&b)
print("Difference (first - second):",a-b)
print("Symmetric difference:",a^b)
