f=open('power.txt', 'w')


for num in range(1,11):
    second=num**2
    third=num**3
    f.write((str(num)+","+ str(second)+","+str(third)+"\n"))

f.close()