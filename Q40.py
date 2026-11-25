# Write a Python program to find common elements between two lists.

a=[int(x) for x in input("First list: ").split()]
b=[int(x) for x in input("Second list: ").split()]
common=[]
for x in a:
    if x in b and x not in common: common.append(x)
print("Common elements:",common)
