def f(t):
    import re
    result=[]
    z=re.findall("\d+",t)
    for liczb in z:
        if len(liczb)==2:
            result.append(liczb)
    print(result)



f("16, 2, 114 33 oraz 1024 a także 8")
