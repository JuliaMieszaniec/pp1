array=[
    [3,7,12,3,9],
    [4,7,8,5,17],
    [2,7,11,6,0]
]
b=array.copy()
z=b[0]
b[0]=b[2]
b[2]=z

for i in b:
    for h in i:
        print(h, end=" ")
    print()