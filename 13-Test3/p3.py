def f1(tekst):
    import re
    names=re.findall("[A-Z][a-z]+",tekst)
    ages=re.findall("\d+", tekst)
    print(names)
    print(ages)

    result={}
    for i in range(len(names)):
        result[names[i]]=ages[i]
        
    print(dict(sorted(result.items())))

def f2(d):
    import re
    ages=re.findall("\d+", d)
    suma=0
    for i in ages:
        suma+=int(i)
    print(suma)



f1("Mark is 24 and Ann is 27")
f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!") 
f2("Mark is 24 and Ann is 27")
f2("Peter is 11, Barbara is 7 and their grandfather John is 103!!") 
