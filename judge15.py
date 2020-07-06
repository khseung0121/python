age = int(input())
balance = 9000
if age >= 7:
    if age <= 12:
        print(balance - 650)
    elif age <= 18:
        print(balance - 1050)
    else:
        print(balance - 1250)
else:
    print('아무것도 해당하지 않음')

    
