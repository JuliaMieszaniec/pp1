f=open('liczby1000.txt', 'w')

import random 

for num in range(50):
    a=random.randint(100,1000)
    f.write((str(a)+"\n"))

f.close()