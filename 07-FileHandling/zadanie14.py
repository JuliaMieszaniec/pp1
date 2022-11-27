file_name=input('podaj nazwe pliku:')
f=open(file_name,'r')
sum=0
for line in f:
    sum+=1
print(f'File name:{file_name}')
print(f'Numbers of lines:{sum}')

f.close()