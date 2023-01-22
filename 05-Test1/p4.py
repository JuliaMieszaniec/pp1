def f(no, even):
    sum=0
    number=str(no)
    if even == True:
        for i in number:
            if int(i)%2==0:
                sum+=int(i)
    else:
        for i in number:
            if int(i)%2!=0:
                sum+=int(i)

    print(sum)

f(3124,True) 
f(3124,False) 
f(20576,False) 
f(20576,True) 
f(13115,True)

def fu(string):
    s=""
    for i in string:
        s+= i+"-"
    print(s[0:-1])
        
        
fu('smart')
