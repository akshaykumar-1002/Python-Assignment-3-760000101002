# Write a Python program to access the first, last and middle elements of a list.

a=[int(x) for x in input("Enter list elements: ").split()]
if a:
    print("First:",a[0])
    print("Last:",a[-1])
    print("Middle:",a[len(a)//2])
else: print("List is empty.")
