import re
class C:
    @staticmethod
    def m1(n):
        a=str(n)
        x=re.findall("\d",a)
        print(x)
        for i in x:
            if int(i)%2 == 0:
                x.remove(i)
        print(x)
        liczba=""
        for h in x:
            liczba+=h
        print(liczba)


C.m1(4231564)
C.m1(79381)
