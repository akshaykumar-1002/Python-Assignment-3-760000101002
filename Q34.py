# Write a Python program to delete an element from a specified index using pop().

a=[int(x) for x in input("Enter list elements: ").split()]
p=int(input("Index to remove: "))
if -len(a)<=p<len(a): print("Removed:",a.pop(p))
else: print("Invalid index.")
print("List:",a)
