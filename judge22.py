num1,num2=map(int,input().split())
total=[2**i for i in range(num1,num2+1)]
del total[1]
del total[-2]
print(total)
