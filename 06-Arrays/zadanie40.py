array=[[-38, 19], [5,40],[-7,11],[29,16]]
max=array[0][0]
min=array[0][0]
rowmin=0
kolumnmin=0
for arr in array:
    for a in arr:
        if a> max:
            max=a

        elif a< min:
            min=a
j=0
h=0
for i in array:
    if min in i:
        print(min,'row',h)
    if max in i:
        print(max,'row',j)
    j+=1
    h+=1


print(min)
print(max)
