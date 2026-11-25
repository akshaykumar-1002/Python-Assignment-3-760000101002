# Write a Python program to demonstrate tuple immutability and create a modified tuple using concatenation.

t=(10,20,30)
print("Original tuple:",t)
print("Tuples are immutable; items cannot be changed directly.")
v=int(input("Enter value to add: "))
new_t=t+(v,)
print("Modified tuple using concatenation:",new_t)
