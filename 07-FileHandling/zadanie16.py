import shutil
f=open('tekstdlugi.txt','r')
z=open('copy.txt','r')

shutil.copyfile('tekstdlugi.txt','copy.txt')
print(z)

z.close()
f.close()