def median(array):
    array.sort()
    print(array)

    x=len(array)
    mid=0
    mid1=0
    suma=0

    if x%2!=0:
        mid=x//2
        print(array[mid])
    else:
        mid=x//2
        mid1=mid -1
        suma= float((array[mid]+array[mid1])/2)
        print(suma)

median([1,6,3,8,2,9])