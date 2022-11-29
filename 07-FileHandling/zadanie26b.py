import re
with open ('tekst.txt',"r") as file:
    z=re.findall("\W+", file.read())

    x=0
    for i in z:
        if len(z[x])>=6:
            print(z[x])
        x+=1
