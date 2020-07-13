x, y = map(int, input().split())
def calc(x, y):##아래를 보니 calc라는 함수를 호출했습니다. 따라서 해당 이름으로 함수를 만들어줍니다.
    return x+y, x-y, x*y, x/y

a, s, m, d = calc(x, y)##return값이 a,s,m,d에 순서대로 들어갑니다.
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
