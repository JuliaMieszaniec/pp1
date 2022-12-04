def f(d):
    sum=0
    for key, values in d.items():
        for val in values:
            if val >= 5 and val<= 10 :
                sum+=val
    
    print(sum)

f({"arr1":[2,6,5],"arr2":[7,1],"arr3":[2,9,8,1]})
