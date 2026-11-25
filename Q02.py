# Write a Python program to count the number of vowels in a given string.

s=input("Enter a string: ")
print("Number of vowels:",sum(1 for c in s if c.lower() in "aeiou"))
