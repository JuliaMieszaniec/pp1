a=[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
a[0][0]=1
a[1][1]=1
a[2][2]=1

print(a)

for i in a:
    for j in a[0]:
        print(j,end=" ")
    print(end=" \n ")
    for j in a[1]:
        if i == a[0]:
            print(j, end=" ")
    print(end="\n")
    for j in a[2]:
        if i == a[0]:
            print(j, end="")
    print(end=" \n ")
    