def f(array):
    count=0
    for arr in array:
        if arr%2 == 0 and arr>8:
            count+=1
    
    print(count)

f([13,7,8,46,6,3,9,12])


