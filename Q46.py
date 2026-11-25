# Write a Python program to create a tuple and access its elements using positive and negative indexing.

t=tuple(input("Enter tuple elements separated by spaces: ").split())
if t:
    print("Tuple:",t)
    print("First:",t[0])
    print("Last:",t[-1])
else: print("Tuple is empty.")
