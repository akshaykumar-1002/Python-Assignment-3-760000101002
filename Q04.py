# Write a Python program to reverse a string without using built-in reverse functions.

s=input("Enter a string: ")
r=""
for c in s:
    r=c+r
print("Reversed string:",r)
