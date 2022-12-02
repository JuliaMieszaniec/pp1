array=[
    [3,7,12,3,9],
    [4,7,8,5,17],
    [2,7,11,6,0]
]
b=array.copy()
i=0
while i < len(array):
    z=array[i][0]
    array[i][0]=array[i][-1]
    array[i][-1]=z

for c in b:
    for h in c:
        print(h, end=" ")
    print()

