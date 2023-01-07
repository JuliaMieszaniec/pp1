cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]

i=0
while i <(len(cars)):
    x="in"
    result=[]
    if cars[i][1] == x:
        result.append(cars[i][0])
    else:
        continue
    i+=1
print(result)
