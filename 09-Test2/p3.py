def f(array2D) :
    i=0
    j=0
    while i < len(array2D):
        while j < (len(array2D)):
            array2D[0][i]+=array2D[j+1][i]
            j+=1
        i+=1
    
    print(array2D)

f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) 