a=[[True, False],[True,True],[False, False]]

for x in a:
    for y in x:
        if y == True:
            y=False
        else:
            y=True
        
print(a)    
