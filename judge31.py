def fib(n):
    if n == 0: # 피보나치 수는 0과 1로 시작하므로 0, 1을 각각 0, 1로 설정합니다.
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2) # 다음번 피보나치 수는 바로 앞의 두 피보나치 수의 합이므로
                             # 문자 그대로 적어줍니다.
n = int(input())
print(fib(n))
