n=int(input())
for i in range(1,n+1):
    for j in range(n):
        if j >= (n-i):
            print('*',end='')
        else:
            print(' ',end='')
    print('*'*(i-1))
