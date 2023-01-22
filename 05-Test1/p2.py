def f(b):
    count=0
    for i in b:
        if i=="0" or i=="1":
            count+=1
    
    if count==len(b):
        print(True)
    else:
        print(False)

f("101101")
f("1311a10100")
