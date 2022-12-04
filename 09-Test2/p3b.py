def f(array):
    result=[]
    sum=0
    for i in range(len(array[0])):
        for j in range(len(array)):
            sum+=array[j][i]
        result.append(sum)
        sum=0 
    print(result)


f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) 