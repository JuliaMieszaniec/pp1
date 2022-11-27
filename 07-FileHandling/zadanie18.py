f1=open('GrainsAndBread.txt','r')
data1=f1.read()
f2=open('MeatAndFish.txt','r')
data2=f2.read()
data1+= "\n"
data1+= data2
f3=open('shoppinglist.txt','w')
f3.write(data1)

f1.close()
f2.close()
f3.close()
