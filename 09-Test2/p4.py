def f(dictionary,x,y):
    sum=0
    for key, value in dictionary.items():
        for v in value:
            if v>=x and v<=y:
                sum+=v
    print(sum)

f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6)
f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10) 
