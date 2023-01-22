def f(ex):
    import re
    znaki=re.findall("[+]",ex)
    liczby=re.findall("[0-9]", ex)
    print(znaki)
    print(liczby)
    wyrazenie=0
    i=0
    wyrazenie=int(liczby[i])
    while i <len(znaki):
        if znaki[i]=="+":
            wyrazenie+=int(liczby[i+1])
        else:
            wyrazenie-=int(liczby[i+1])
    
    print(wyrazenie)

f("5+3")
f("1-3+5-1-2+10")
