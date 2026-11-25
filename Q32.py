# Write a Python program to append five elements to an existing list.

a=[int(x) for x in input("Enter existing list: ").split()]
for i in range(5): a.append(int(input(f"Enter element {i+1}: ")))
print("Updated list:",a)
