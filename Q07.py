# Write a Python program to count the number of digits, alphabets and special characters in a string.

s=input("Enter a string: ")
d=sum(1 for c in s if c.isdigit())
a=sum(1 for c in s if c.isalpha())
sp=sum(1 for c in s if not c.isalnum())
print("Digits:",d)
print("Alphabets:",a)
print("Special characters:",sp)
