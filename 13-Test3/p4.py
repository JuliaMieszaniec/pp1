cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]


for i in range(len(cars)):
    x="in"
    result=[]
    result2=[]
    if cars[i][1] == x:
        z=cars[i][0]
        result.append(z)
    else:
        z=cars[i][0]
        result2.append(z)

print(result)
print(result2)
