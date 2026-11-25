# Write a Python program to check whether a given string is a palindrome.

s=input("Enter a string: ")
t=s.replace(" ","").lower()
print("Palindrome" if t==t[::-1] else "Not a palindrome")
