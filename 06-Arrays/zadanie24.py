nums=[2, 3, 2, 5, 8, 1, 9, 8]

nums.sort()
print(nums)
liczba1=nums[0]
liczba2=nums[1]
z=0
while z < len(nums):
    if liczba1==liczba2:
        nums.remove(liczba1)
        liczba1=liczba2
        z+=1
        liczba2=nums[z+1]
    else:
        liczba1=liczba2
        z+=1
        liczba2=nums[z+1]
print(nums)

