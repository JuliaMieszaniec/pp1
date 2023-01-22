def f(pat):
    liczba=pat//5
    reszta=pat%5
    monety=0
    monety+=liczba
    liczba=reszta//2
    reszta=reszta%2
    monety+=liczba
    monety+=reszta
    print(monety)

f(23)
f(8) 
f(2) 
f(0) 


def fu(string):
    for i in range(3):
        h=(i+1)*(-1)
        count=0
        if string[i]== string[h]:
            count+=1


    if count==(len(string)//2):
        print(True)
    else:
        print(False)

fu("abcdcba")