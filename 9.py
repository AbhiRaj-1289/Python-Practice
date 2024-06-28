import sys
s = sys.argv[1]
special = "~`!@#$%^&*()_+{}|:?><[/].,\;'[]"
lower = 0
upper = 0
other = 0
for char in s:
    if(char.islower()): 
        lower += 1
    if(char.isupper()): 
        upper += 1
    if char in special:
        other += 1
print("No. Of Uppercase Characters = ",upper)
print("No. Of Lowercase Characters = ",lower)
print("No. Of Other Characters = ",other)