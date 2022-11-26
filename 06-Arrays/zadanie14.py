a=[
    ['true', 'false'],
    ['true', 'true'],
    ['false','false']]

for x in a:
    for y in x:
        if y == 'true':
            y='false'
        elif y=='false':
            y='true'
        
        
print(a)    

