def f(n):
    x=0
    y=0
    if n<=0:
        print("")
    else:
        x=n//5
        y=n%5
        if y==0:
            print("/////-"*(x-1)+"/////")
        else:
            print(("/////-"*x) + ("/"*y) )


f(-4)
f(0)
f(5)
f(7)
f(10)
f(11)