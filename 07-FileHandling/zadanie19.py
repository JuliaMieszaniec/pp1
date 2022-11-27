f=open('liczby50.txt', 'w')

for num in range(1,51):
    f.write(str(num)+"\n")


f.close()