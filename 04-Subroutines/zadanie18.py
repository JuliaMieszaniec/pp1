def sumaliczb(n):
    sum=0
    while(n!=0):
        sum=sum + int(n%10)
        n=int(n/10)
    return sum

print(sumaliczb(7182))