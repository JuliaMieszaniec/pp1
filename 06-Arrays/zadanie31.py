array=[1,4,3,2,8,4,7,9,12,5]
list1=[]
list2=[]

for arr in array:
    if arr%2==0:
        list1.append(arr)
    else:
        list2.append(arr)

print(list1 + list2)