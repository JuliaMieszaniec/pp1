def read_number():
    x=int(input('Enter number:'))
    return x

def generate_number():
    import random
    a=random.randint(1,10)
    return a

z=read_number()
b=generate_number()
print(z)
print(b)

if z==b:
    print('Winner!')
else:
    print('Loser')