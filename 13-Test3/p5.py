class C():
    def __init__(self,array):
        self.sum=0
        self.array=array
        self.name=""
        for arr in self.array:
            self.sum+=arr
        for z in range(len(self.array)-1):
            self.name+=str(self.array[z])
            self.name+="+"
        self.name+= str(self.array[-1])

        

    def __str__(self):
        return f"{self.name}={self.sum}"
 
print(C([5,12]))
