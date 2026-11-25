# Write a Python program to check whether two strings are equal, ignoring their case.

a=input("First string: ")
b=input("Second string: ")
print("Equal ignoring case:",a.casefold()==b.casefold())
