list1 = [1,2,1,1,4,3,2,7,6,7]
list2 =[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)