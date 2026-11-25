# Write a Python program to find the first and last occurrence of a character using string methods.

s=input("Enter a string: ")
c=input("Enter one character: ")
if len(c)==1:
    print("First occurrence:",s.find(c))
    print("Last occurrence:",s.rfind(c))
else: print("Enter exactly one character.")
