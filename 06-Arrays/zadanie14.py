import array as a

a=[
    ['true', 'false'],
    ['true', 'true'],
    ['false','false']
]
for h in range(0, len(a)):
        if h == 'true':
            h='false'
        elif h=='false':
            h='true'
        print(a)

for x in a:
    for y in x:
        if y == 'true':
            y='false'
        elif y=='false':
            y='true'
            
print(a)
