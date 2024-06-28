#Code to count number of uppercase, lowercase and special characters in the string inputted as command line
#Author : Abhinav Raj

import sys
if len(sys.argv) < 2:
    print("Please provide a string as a command line argument.")
    sys.exit(1)

s = sys.argv[1]
special = "~`!@#$%^&*()_+{}|:?><[/].,;'[]\\\""
lower = 0
upper = 0
other = 0

for char in s:
    if char.islower(): 
        lower += 1
    elif char.isupper(): 
        upper += 1
    elif char in special:
        other += 1

print("No. Of Uppercase Characters =", upper)
print("No. Of Lowercase Characters =", lower)
print("No. Of Other Characters =", other)
