array=[
    [7,3,7,9,0],
    [2,9,0,1,5],
    [3,8,6,4,7],
    [8,7,1,1,5]
]
suma=0
for arr in array[3]:
    suma+=arr
print(suma) 


i=0
sum=0
while i<len(array):
    sum+=array[i][4]
    i+=1

print(sum)

