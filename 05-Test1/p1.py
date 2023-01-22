def f(no):
    gwiazdki="*"*10
    print(no[0]+no[1]+gwiazdki+no[12]+no[13]+no[14]+no[15])


f("5290312400019022") 

def fu(znaki):
    x=znaki.count("+")
    z=znaki.count("-")
    if x==z:
        print(True)
    else:
        print(False)

fu("++-+")
fu("++--")
