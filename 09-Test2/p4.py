def f(dictionary,x,y) :
    import re

    x=re.findall("[0-9]",dictionary)
    print(x)

f(([0,2,7,87,9]),2,9) 
