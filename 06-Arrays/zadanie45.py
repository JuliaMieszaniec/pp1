def convert(array):
    array[0]+=array[1]
    array.remove(array[1])
    return array

arr=[[2,3],[1,5]]
print(convert(arr))

convert([[2,3],[1,5]])
convert([[5,0,3,7,5],[9,0,9,1,2]])
