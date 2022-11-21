f=open('addnames.txt','w')

for i in range(5):
    zakupy=input(':')
    f.write(f'{zakupy}\n')

f.close()