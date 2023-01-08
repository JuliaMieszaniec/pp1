class C:
    def __init__(self,count):
        self.counter=count
    def m1(self):
        print(self.counter)
    def m2(self):
        self.counter+=1
    def m3(self):
        self.counter-=1
    def m4(self,n):
        self.counter+=n

c=C(5)
c.m1()
c.m2()
c.m1()
c.m4(-8)
c.m1()
c.m3()
c.m1()
c.m4(10)
c.m1() 
