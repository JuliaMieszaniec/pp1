arr=[1,2,3,4,5]
arr[0] -= 1
arr[-1] += 4
mid=int(len(arr)/2)
arr[mid]*= 2
for x in arr:
    x= x+ 3
    print(x, end=" ")
print('')

for x in range (0, len(arr)):
    arr[x]+= 3

print(arr)