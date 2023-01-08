class Statistics:
    def __init__(self):
        self.array=[]

    def set_no(self,numbers):
        self.array+=numbers
        a=int(input("Podaj liczbe:"))
        self.array.append(a)

    def display(self):
        for i in self.array:
            print(i, end=" ")

    def smallest(self):
        min=self.array[0]
        for i in self.array:
            if i < min :
                min=i
        print(min)
        
    def biggest(self):
        max=self.array[0]
        for i in self.array:
            if i > max :
                max=i
        print(max)

    def srednia(self):
        suma=0
        for i in self.array:
            suma+=i
        srednia=suma/(len(self.array))
        print(srednia)
    
    def mediana(self):
        self.array.sort()
        mid=0
        if len(self.array)%2 == 0:
            mid=len(self.array)//2
            mid=(self.array[mid]+ self.array[mid-1])/2
            print(mid)

        else:
            mid=len(self.array)//2
            print(self.array[mid])

stat=Statistics()
stat.set_no([12, 37, 6, 9, 17 ])
stat.display()
stat.smallest()
stat.biggest()
stat.srednia()
stat.mediana()
