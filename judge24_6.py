price=list(map(int,input().split(';')))
price.reverse()
for i in range(len(price)):
    print('{0:9,}'.format(price[i]))
    
