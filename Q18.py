# Write a Python program to find the longest word in a given sentence using string operations.

words=input("Enter a sentence: ").split()
if words: print("Longest word:",max(words,key=len))
else: print("No words entered.")
