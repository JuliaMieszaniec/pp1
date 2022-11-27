f=open('tekstdlugi.txt','r')

x=0
for line in f:
    print(line)
    x+=1
    if x%5==0:
        try:
            d=input('naciścnij zeby iśc dalej')
        except:
            break
