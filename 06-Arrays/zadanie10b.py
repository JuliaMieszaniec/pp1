li=[1,2,3,4,5,6,7,8,9]
even=0
odd= int(len(li)-even)

for y in li:
    while (y%2==0):     
        even+=1

print(f'even1:{even} odd1:{odd}')


list1 = [10, 21, 4, 45, 66, 93, 1]
 
even_count, odd_count = 0, 0
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1
 
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)