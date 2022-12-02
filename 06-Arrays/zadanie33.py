import random

a=[random.randint(1,1000) for i in range(8)]

for i in range(39):
    print("-", end="")
print()
for i in a:
    print("|",i,end="")
print("|")
for i in range(39):
    print("-",end="")