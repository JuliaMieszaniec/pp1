import re
mess="To be, or not to be, that is the question"
a=re.findall("a", mess)
e=re.findall("e", mess)
i=re.findall("i", mess)
o=re.findall("o", mess)
u=re.findall("u", mess)
y=re.findall("y", mess)

suma=len(a)+len(e)+len(i)+len(o)+ len(u)+len(y)
print(suma)
