def f(player1,player2):
    sum1=0
    sum2=0
    for nums in player1:
        if nums == "A" or "K" or "Q"or "J" or "T":
            sum1+=10
        else:
            sum1+=int(nums)

    for num in player2:
        if num == "A" or "K" or "Q"or "J" or "T":
            sum2+=10
        else:
            sum2+=int(num)

    if sum1 > sum2:
        print(True)
    else:
        print(False)


f("AJ972","AQT72") 
f("9532","K8") 
f("987","AT4") 