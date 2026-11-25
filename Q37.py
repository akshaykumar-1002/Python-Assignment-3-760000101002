# Write a Python program to find the second-largest element in a list.

a=[int(x) for x in input("Enter numbers: ").split()]
u=sorted(set(a),reverse=True)
if len(u)>=2: print("Second-largest:",u[1])
else: print("Enter at least two distinct values.")
