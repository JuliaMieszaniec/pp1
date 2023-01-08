import math
class Statistic():
    @staticmethod
    def trojkat(a,h):
        print((a*h)/2)

    @staticmethod
    def kolo(r):
        print(math.pi*(r**2))

    @staticmethod
    def prostokat(a,b):
        print(a*b)

print(Statistic.kolo(3))
print(Statistic.trojkat(6,2))
print(Statistic.prostokat(4,7))
