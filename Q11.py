# Write a Python program to count the occurrences of a particular character in a string.

s=input("Enter a string: ")
c=input("Enter one character: ")
if len(c)==1: print("Occurrences:",s.count(c))
else: print("Enter exactly one character.")
