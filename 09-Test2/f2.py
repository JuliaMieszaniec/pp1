def f(array1,array2):
    c1=0
    c2=0
    for a in array1:
        if a >=10 and a<100:
            c1+=1
    for arr in array2:
        if arr >=10 and arr<100:
            c2+=1
        
    if c1==c2:
        print(True)
    else:
        print(False)

f([23,7,16,34],[1,18,79,20,6,111])