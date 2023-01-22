def f(nazwa):
    caly=""
    import re
    x=re.split("\s", nazwa)
    print(x)
    for num in x:
        nums=num[0]
        caly+=nums

    print(caly)
