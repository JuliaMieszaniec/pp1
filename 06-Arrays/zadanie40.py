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

print(min)
print(max)
