li=[-15,8,-31,47,-2,19]
min=li[0]
max=li[0]
for x in li:
    if x>max:
        max=x
    if x< min:
        min=x

print(f'max {max}')
print(f'min {min}')
