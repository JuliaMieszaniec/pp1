import array as a

a=[
    [3, 9, 2],
    [2, 4, 5],
    [7, 1, 6],
    [0, 4, 8]
]
suma=0
for x in a:
    if x%2==0:
        suma+=x
    print(suma)