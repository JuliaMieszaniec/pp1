x = 4
for i in range(5):
    if i % 2 == 0:
        continue
    x += 1

print(x)
import re
txt="1.22.333.4444.55555.666666"
y=re.findall("\d+", txt)
print(y)

h = 'to be or not to be'
z = h[0b11:0xB]
g=h[3:11]
print(g)

print('uniwersytet'[3:8])
