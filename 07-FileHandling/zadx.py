file = open('krotkitekst.txt','r')
file_content = file.read()
#pokaże cały tekst
print( file_content )

#liczba znaków w pliku(łacznie ze spacjami itp.)
liczba_znakow_w_pliku=len(file_content)
print(liczba_znakow_w_pliku)

#liczba wierszy w pliku
import re
wiersze=re.findall(".+", file_content)
print(len(wiersze))

#liczba słów w pliku
slowa=re.findall("\S+", file_content)
print(len(slowa))

#liczy średnią długości słowa
i=0
srednia=0
while i<len(slowa):
    liczba_znaków_pojedynczego_słowa=len(slowa[i])
    a=int(liczba_znaków_pojedynczego_słowa)
    srednia+=a
    i+=1
srednia=srednia/len(slowa)
print(srednia)


file.close()
