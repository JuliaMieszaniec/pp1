def f(human_age) :
    dogage=0
    if human_age == 1 :
        dogage=10
    elif human_age == 2:
        dogage=20
    else:
        dogage+=20
        dogage+= ((human_age-2)*4)

    print(dogage)

f(15)
f(2)