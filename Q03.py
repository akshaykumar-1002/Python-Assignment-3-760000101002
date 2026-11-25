# Write a Python program to count vowels and consonants separately in a string.

s=input("Enter a string: ")
v=sum(1 for c in s if c.lower() in "aeiou")
con=sum(1 for c in s if c.isalpha() and c.lower() not in "aeiou")
print("Vowels:",v)
print("Consonants:",con)
