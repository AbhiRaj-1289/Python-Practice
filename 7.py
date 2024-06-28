#Code to count number of vowel in the input string
#Author : Abhinav Raj

string = input("Enter a string : ")
vowel = "aeiouAEIOU"
count = 0
for i in string:
    if i in vowel:
        count += 1
print("Vowel Count = ",count)