# Write a Python program to remove duplicate elements from a list.

a=[int(x) for x in input("Enter numbers: ").split()]
result=[]
for x in a:
    if x not in result: result.append(x)
print("Without duplicates:",result)
