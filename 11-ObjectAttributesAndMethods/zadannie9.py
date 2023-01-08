class Arrays():

    def f(num1, num2):
        array=[]
        for x in range(num1):
            array.append(num2)
        print(array)

    def create_random(num1,num2, num3):
        import random
        array=[]
        for h in range(num1):
            x=random.randrange(num2,num3)
            array.append(x)
        print(array)

    def form_to_arr(array,value_from, value_to):
        licznik=0
        for i in array:
            if i>value_from and i<=value_to:
                licznik+=1
        print(licznik)



Arrays.f(5,8)
Arrays.create_random(20,-7,8)
Arrays.form_to_arr([1,2,3,4,5,-1,0],-1,2)

