def sum(N):
    if N==1:
        return 1
    if N>1:
        return N + sum(N-1)
print(f'Suma wynosi: {sum(10)}')
