li=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest=(len(li[0]))
zmienna=li[0]

for x in li:
    if len(x) > longest :
        longest=len(x)
        zmienna=x

print(zmienna)