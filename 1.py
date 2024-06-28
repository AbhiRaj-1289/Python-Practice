#Removing empty list from the following list
#Author : Abhinav Raj

list1 = [[1,2,3],[],['a','b','c'],[]]
for i in list1:
	if i == []:
		list1.remove(i)
print(list1)