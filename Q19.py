# Write a Python program to count the frequency of each character in a string.

s=input("Enter a string: ")
freq={}
for c in s: freq[c]=freq.get(c,0)+1
for c,n in freq.items(): print(repr(c),":",n)
