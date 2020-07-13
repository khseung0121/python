int1, int2 = map(int,input().split())
a={i for i in range(1, int1 + 1) if int1 % i == 0}
##range범위를 0부터 시작하게 되면 0으로 나누는 오류를 범하게 됩니다.
b={i for i in range(1, int2 + 1) if int2 % i == 0}
divisor = a & b ##a와 b의 교집합을 의미합니다.

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)
