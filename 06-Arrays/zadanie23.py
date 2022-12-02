def bubblesort(array):
    n=len(array)

    for i in range(n-1):
        flag=0

        for j in range(n-1):
            if array[j]> array[j+1]:
                tmp=array[j]
                array[j]=array[j+1]
                array[j+1]= tmp
                flag=1

        if flag == 0:
            break

    return array

el=[21,6,9,33,3]
result=bubblesort(el)
print(result)
