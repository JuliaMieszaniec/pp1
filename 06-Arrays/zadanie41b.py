array=[
    [3,7,12,3,9],
    [4,7,8,5,17],
    [2,7,11,6,0]
]
b=array.copy()
b.pop(0)
b.insert(0,[6,7,8,9,10])
b.pop(2)
b.insert(2,[6,7,8,9,10])

for i in b:
    for h in i:
        print(h, end=" ")
    print()