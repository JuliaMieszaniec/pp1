import re
mess="To be, or not to be, that is the question"
x=re.split("\s", mess)
print(len(x))
y=re.findall("\s",mess)
print(len(y)+1)
