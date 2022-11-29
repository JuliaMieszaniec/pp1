import re
f=open('grades.txt',"r")
f_content=f.read()

numbers=re.findall("\d.\d",f_content)
print(numbers)
suma=0
ilosc=len(numbers)
print(ilosc)
for number in numbers:
    suma+=float(number)

print(suma)
srednia=float(suma/ilosc)
print(srednia)
f.close()