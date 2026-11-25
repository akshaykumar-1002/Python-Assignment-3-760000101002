# Write a Python program to count uppercase and lowercase characters in a string.

s=input("Enter a string: ")
u=sum(1 for c in s if c.isupper())
l=sum(1 for c in s if c.islower())
print("Uppercase:",u)
print("Lowercase:",l)
