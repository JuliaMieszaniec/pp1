array=[
    [3,7,12,3,9],
    [4,7,8,5,17],
    [2,7,11,6,0]
]
b=array.copy()
i=0
while i < len(b):
    z=b[i][0]
    b[i][0]=b[i][-1]
    b[i][-1]=z

print(array)
print(b)
