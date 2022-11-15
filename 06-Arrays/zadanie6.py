li = [2,3,7,5,4]

print('a', li)
print('b', len(li))
print('c', li[0])
print('d', li[1])
print('e', li[len(li)-1])
print('f', li[len(li)-2])
print('g', li[0]+ li[len(li)-1])
print('h', li[int(len(li)/2)])
print('i', )
for x in li:
    print(x, end=" ")
print('')
print('j')
for x in range (0,int(len(li)/2)+ 1):
    print(li[x], end=" ")
    