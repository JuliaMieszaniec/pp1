def minmax(array):
    smallest=array[0]
    largest=array[0]
    newarray=[]

    for arr in array:
        if arr> largest:
            largest=arr
        elif arr< smallest:
            smallest=arr

    newarray.append(smallest)
    newarray.append(largest)
    print(newarray)

minmax([4,2,8,4,7,9,5])