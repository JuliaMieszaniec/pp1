def identity_matrix(n):
    arr=[[0 for i in range(n)]for j in range(n)]
    z=0
    while z<n:
        arr[z][z]=1
        z+=1
    
    for h in arr:
        print(h)
    print()



identity_matrix(3)