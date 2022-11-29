import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
print(temperatures)
suma=0
ilosc=len(temperatures)
for temp in temperatures:
    suma= int(suma) + int(temp)

srednia=suma//ilosc   
print(int(suma))
print(srednia)
