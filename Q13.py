# Write a Python program to check whether a given string starts and ends with a particular character.

s=input("Enter a string: ")
c=input("Enter one character: ")
if len(c)==1:
    print("Starts with:",s.startswith(c))
    print("Ends with:",s.endswith(c))
else: print("Enter exactly one character.")
