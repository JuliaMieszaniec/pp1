array=[5,1,9,6,1]
largest=array[0]
smallest=array[0]

for arr in array:
    if arr > largest:
        largest=arr
    elif arr < smallest:
        smallest= arr
        
print(largest, smallest)
print(largest-smallest)