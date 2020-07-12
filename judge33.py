def countdown (n):
    cnt = n + 1 #출력할 지역변수를 만들어줍니다. 하나씩 줄일 것이므로 +1 해주었습니다.
    def cntdown():
        nonlocal cnt # 클로저의 지역 변수를 변경하기 위해 nonlocal을 사용합니다.
        cnt -= 1
        return cnt # 이 값이 print(c())에 들어가게 하기 위함입니다.
    return cntdown
n = int(input())

c = countdown(n) # cntdown을 리턴하였으므로  c에는 함수 cntdown이 들어갑니다.
for i in range(n):
    print(c(), end=' ')
