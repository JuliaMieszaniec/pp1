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


def fu(ex):
    import re
    znaki=re.findall("-|[+]",ex)
    liczby=re.findall("\d+", ex)
    print(znaki)
    print(liczby)
    wyrazenie=0
    i=0
    wyrazenie=int(liczby[i])
    while i <len(znaki):
        if znaki[i]=="+":
            wyrazenie+=int(liczby[i+1])
            i+=1
        else:
            wyrazenie-=int(liczby[i+1])
            i+=1
        
    
    print(wyrazenie)

fu("5+3")
fu("1-3+5-1-2+10")
