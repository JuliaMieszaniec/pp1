for x in range(1,31):
    if x%3==0 and x%5!=0:
        print('THREE')
    if x%5==0 and x%3!=0:
        print('FIVE')
    if x%5==0 and x%3==0:
        print('BINGO')
    if x%5!=0 and x%3!=0:
        print(x)
 