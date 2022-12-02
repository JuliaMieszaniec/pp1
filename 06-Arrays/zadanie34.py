def check(a1,a2):
    for i in a1:
        if i not in a2:
            return False
    return True


x=[5,4,3,1]
y=[6,5,4,3,2]

print(check(x,y))
